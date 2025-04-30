Building a Web-Based Light Scheduler with WebSocket and MQTT

FILE STRUCTURE
--------------
1. communication.py — WebSocket server that receives commands from the UI and publishes them to an MQTT broker.
2. lightschedule.py — MQTT subscriber that listens for commands and sends them to a (simulated or real) Arduino via serial.
3. light.ino — Arduino sketch to control a relay based on serial commands (ON or OFF).
4. Simulation.py — A fake Arduino environment to test without real hardware.
5. index.html — Web-based UI to input schedule times.
6. script.js — JavaScript for UI interactivity and WebSocket communication.

REQUIREMENTS
------------

1. Python 3.7+
2. Arduino IDE
3. A virtual serial interface
4. MQTT broker
Python packages: paho-mqtt websockets pyserial
Simulation Setup 
Run the fake Arduino:

python simulation.py
Start the WebSocket server:

python communication-socket.py
Start the MQTT scheduler listener:

python lightScheduler.py
Open index.html in your browser and set schedule times.

USAGE
------

Input On Time and Off Time in the UI.
Click Submit.
The schedule is:
Sent via WebSocket to communication-socket.py
Published to MQTT
Received by schedule-light.py
Sent to the Arduino (or simulator)
Executed at the scheduled time


Credits
Author IRADUKUNDA Joyeuse

SUbmission of the evaluation.


