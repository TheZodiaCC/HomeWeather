import time
from grove.i2c import Bus


class Station(object):

    def __init__(self, address=0x44, bus=None):
        self.address = address

        self.bus = Bus(bus)

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

    def read(self):
        self.bus.write_i2c_block_data(self.address, 0x24, [0x00])

        time.sleep(0.016)

        data = self.bus.read_i2c_block_data(self.address, 0x00, 6)

        temperature = data[0] * 256 + data[1]
        celsius = -45 + (175 * temperature / 65535.0)
        humidity = 100 * (data[3] * 256 + data[4]) / 65535.0

        return celsius, humidity
