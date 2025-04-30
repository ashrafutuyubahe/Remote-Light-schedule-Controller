# MQTT Remote Scheduler 🕒 🔌

A web-based MQTT scheduling system that controls an Arduino relay based on user-defined schedules through a modern web interface.

## Project Overview 🎯

This project implements a remote relay control system using MQTT protocol and WebSocket communication:
- A web interface for setting ON/OFF times
- A WebSocket server that forwards schedules to MQTT
- A Python subscriber that receives schedules and controls Arduino
- An Arduino sketch that controls a physical relay (LOW = ON, HIGH = OFF)

## Components 🔧

### 1. Web Interface 🌐
- Modern, responsive design using Bootstrap
- Real-time schedule updates via WebSocket
- Simple time input fields for ON/OFF scheduling

### 2. WebSocket Server (`websocket_server.py`) 🔄
- Handles web client connections
- Maintains schedule checking (every 3 seconds)
- Publishes ON/OFF commands to MQTT at scheduled times

### 3. MQTT Subscriber (`subscriber.py`) 📥
- Receives commands from MQTT broker
- Manages serial communication with Arduino
- Provides detailed logging of all operations

### 4. Arduino Controller (`arduino/relay.ino`) ⚡
- Controls physical relay on pin 7
- LOW = Light ON, HIGH = Light OFF
- Includes debug serial output

## Setup Requirements 📋

1. Hardware 🛠️:
   - Arduino board
   - Relay module connected to pin 7
   - USB connection between Arduino and computer

2. Software Dependencies 💻:
   - Python 3.x
   - Required Python packages (install via `pip install -r requirements.txt`):
     - paho-mqtt
     - pyserial
     - websockets
   - Arduino IDE for uploading the sketch
   - Modern web browser

## Configuration ⚙️

1. MQTT Broker:
   - Default broker IP: 157.173.101.159
   - Default port: 1883
   - Topic: relay/controll

2. Serial Communication:
   - Default port: /dev/ttyACM0
   - Baud rate: 9600

3. Web Interface:
   - HTTP server: http://localhost:8000
   - WebSocket server: ws://localhost:8765

## Usage 🚀

1. Upload the Arduino sketch to your board:
   ```bash
   # Using Arduino IDE, upload arduino/relay.ino
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the WebSocket server:
   ```bash
   python websocket_server.py
   ```

4. Start the MQTT subscriber:
   ```bash
   python subscriber.py
   ```

5. Open http://localhost:8000 in your web browser
6. Set your desired ON and OFF times and click Submit

## Debug Output 🔍

The system provides detailed logging at each step:

1. WebSocket Server:
   - Shows schedule reception and MQTT publishing
   - Logs schedule checking every 3 seconds

2. MQTT Subscriber:
   - Shows connection status
   - Logs command reception and forwarding
   - Displays Arduino responses

3. Arduino:
   - Confirms command reception
   - Shows relay state changes
   - Reports current light status

## Screenshots 📸

### Web Interface

![The UI from where you will automate the light bulb to ](./embedded.png)


## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing 🤝

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Security Note 🔒

The MQTT broker IP is hardcoded for demonstration purposes. In a production environment, consider:
1. Using environment variables for sensitive configuration
2. Implementing MQTT authentication
3. Using TLS for MQTT and WebSocket connections

## Customization ✨

- Modify the web interface design in `static/style.css`
- Adjust schedule check frequency in `subscriber.py`
- Configure MQTT topics and broker settings in both Python scripts
