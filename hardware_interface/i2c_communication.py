import smbus


def open_i2c_bus(bus_number):
    # Open an I2C bus using smbus or Adafruit-I2C

    bus = smbus.SMBus(bus_number)

    return bus


def write_i2c_data(bus, address, data):
    # Write data to an I2C device

    bus.write_i2c_block_data(address, 0, data)


def read_i2c_data(bus, address, num_bytes):
    # Read data from an I2C device

    data = bus.read_i2c_block_data(address, 0, num_bytes)

    return data
