import paho.mqtt.client as mqtt
import serial
import time

print("=== IoT Light Control Subscriber ===")
print("Initializing MQTT-Serial bridge...")

# Set your serial port and baud rate
try:
    ser = serial.Serial('COM5', 9600, timeout=1)
    print("✓ Serial connection established with Arduino on COM5")
    time.sleep(2)
    initial_msg = ser.readline().decode().strip()
    while initial_msg:
        print(f"[Arduino Init]: {initial_msg}")
        initial_msg = ser.readline().decode().strip()
except Exception as e:
    print(f"✗ Failed to connect to Arduino: {str(e)}")
    raise e

# Store schedule (optional future use)
schedule = {
    'on_time': None,
    'off_time': None
}

def handle_mqtt_connection(client, userdata, flags, rc):
    print(f"✓ Connected to MQTT broker (status code {rc})")
    client.subscribe("relay/controll")
    print("✓ Listening on topic: relay/controll")

def handle_mqtt_command(client, userdata, msg):
    try:
        command = msg.payload.decode().strip()
        print("\n📥 New MQTT Command Received:")
        print(f"> Command Payload: {command}")
        
        if command in ["ON", "OFF"]:
            print(f"→ Sending command to Arduino: {command}")
            ser.write(f"{command}\n".encode())
            
            print("🔁 Awaiting Arduino response...")
            time.sleep(0.1)
            while ser.in_waiting:
                response = ser.readline().decode().strip()
                print(f"[Arduino]: {response}")
        else:
            print(f"⚠️ Unrecognized command: {command}")
            
    except Exception as e:
        print(f"✗ Error handling MQTT message: {str(e)}")

# MQTT setup
client = mqtt.Client()
client.on_message = handle_mqtt_command
client.on_connect = handle_mqtt_connection

print("\nConnecting to MQTT broker...")
client.connect("157.173.101.159", 1883, 60)

# Start MQTT loop
print("🔄 MQTT loop started. Awaiting commands...\n")
client.loop_forever()
