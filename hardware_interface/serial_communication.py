import serial


def open_serial_port(port, baudrate):
    # Open a serial port using PySerial or PyVISA

    ser = serial.Serial(port=port, baudrate=baudrate, timeout=1)

    return ser


def send_serial_data(ser, data):
    # Send data over a serial port

    ser.write(data.encode())


def receive_serial_data(ser):
    # Receive data over a serial port

    data = ser.read(ser.inWaiting()).decode()

    return data
