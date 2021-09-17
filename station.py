import time
from grove.i2c import Bus
import board
from adafruit_lc709203f import LC709203F
from config import Config


class I2C_Station:
    def __init__(self, weather_sensor_address=Config.I2C_WEATHER_SENSOR_ADDRESS, bus=None):
        self.weather_sensor_address = weather_sensor_address
        self.bus = Bus(bus)
        self.powergauge_module = LC709203F(board.I2C(), address=Config.I2C_POWERGAUGE_ADDRESS)

    def CRC(self, data):
        crc = 0xff
        for s in data:
            crc ^= s
            for _ in range(8):
                if crc & 0x80:
                    crc <<= 1
                    crc ^= 0x131
                else:
                    crc <<= 1
        return crc

    def read_weather_data(self):
        self.bus.write_i2c_block_data(self.weather_sensor_address, 0x24, [0x00])

        time.sleep(0.016)

        data = self.bus.read_i2c_block_data(self.weather_sensor_address, 0x00, 6)

        temperature = data[0] * 256 + data[1]
        celsius = -45 + (175 * temperature / 65535.0)
        humidity = 100 * (data[3] * 256 + data[4]) / 65535.0

        return celsius, humidity

    def get_power_stats(self):
        try:
            voltage = self.powergauge_module.cell_voltage
            power = self.powergauge_module.cell_percent
        except Exception as e:
            voltage = None
            power = None

        return power, voltage
