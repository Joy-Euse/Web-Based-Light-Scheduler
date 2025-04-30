import serial
import serial.threaded
import time

class FakeArduino(serial.threaded.Protocol):
    def __init__(self):
        super().__init__()

    def data_received(self, data):
        message = data.decode('utf-8').strip()
        print(f"Command received from host: '{message}'")

        if message == "ON":
            print("Simulating relay activation... (ON)")
        elif message == "OFF":
            print("Simulating relay deactivation... (OFF)")
        else:
            print("Unrecognized instruction. Ignored.")

def main():
    print("Initializing virtual Arduino on COM5 (loopback mode)...")
    
    # Open virtual serial port
    ser = serial.serial_for_url('loop://', baudrate=9600, timeout=1)
    protocol = serial.threaded.ReaderThread(ser, FakeArduino)
    protocol.start()
    
    print("Emulator active. Awaiting serial input commands... (ON/OFF)")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Emulator shutdown requested by user.")
        protocol.stop()

if __name__ == "__main__":
    main()
