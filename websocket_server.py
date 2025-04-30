import asyncio
import json
import websockets
import paho.mqtt.publish as publish
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading
from datetime import datetime

# MQTT settings
MQTT_BROKER = "157.173.101.159"
MQTT_TOPIC = "relay/controll"  # Changed back to original topic

# Serve static files
class HttpHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="static", **kwargs)

def run_http_server():
    print("Starting HTTP server on http://localhost:8000")
    server = HTTPServer(('localhost', 8000), HttpHandler)
    server.serve_forever()

async def schedule_controller(on_time, off_time):
    """Check schedule and publish commands at appropriate times"""
    while True:
        current_time = datetime.now().strftime("%H:%M")
        
        if current_time == on_time:
            print(f"Schedule: Time to turn ON ({current_time})")
            publish.single(MQTT_TOPIC, payload="ON", hostname=MQTT_BROKER)
            print("Published ON command")
        
        if current_time == off_time:
            print(f"Schedule: Time to turn OFF ({current_time})")
            publish.single(MQTT_TOPIC, payload="OFF", hostname=MQTT_BROKER)
            print("Published OFF command")
        
        await asyncio.sleep(3)  # Check every 3 seconds

async def handle_websocket(websocket):
    try:
        print("WebSocket connection established")
        async for message in websocket:
            data = json.loads(message)
            on_time = data['onTime']
            off_time = data['offTime']
            
            print(f"Received schedule: ON at {on_time}, OFF at {off_time}")
            
            try:
                # Start schedule checker
                schedule_task = asyncio.create_task(schedule_controller(on_time, off_time))
                
                await websocket.send(json.dumps({
                    'success': True,
                    'message': f'Schedule set: ON at {on_time}, OFF at {off_time}'
                }))
                
                # Keep checking schedule until connection closes
                await schedule_task
                
            except Exception as e:
                print(f"Error in schedule: {str(e)}")
                await websocket.send(json.dumps({
                    'success': False,
                    'message': f'Error setting schedule: {str(e)}'
                }))
    except websockets.exceptions.ConnectionClosed:
        print("WebSocket connection closed")
        pass

async def main():
    print("Starting WebSocket server on ws://localhost:8765")
    # Start HTTP server in a separate thread
    http_thread = threading.Thread(target=run_http_server, daemon=True)
    http_thread.start()

    # Start WebSocket server
    async with websockets.serve(handle_websocket, "localhost", 8765):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
