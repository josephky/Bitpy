__author__ = 'alexisgallepe and Shlomi Zeltsinger'

from Utils.dataTypes import *


class HeaderParser:
    def __init__(self, header):  # Packets is a stream

        self.magic = read_hexa(header.read(4))
        self.command = header.read(12)
        self.payload_size = read_uint32(header.read(4))
        self.checksum = read_hexa(header.read(4))

        self.header_size = 4 + 12 + 4 + 4

    def to_string(self):
        display = "\n-------------HEADER-------------"
        display += "\nMagic:\t %s" % self.magic
        display += "\nCommand name	:\t %s" % self.command
        display += "\nPayload size	:\t %s" % self.payload_size
        display += "\nChecksum	:\t\t %s" % self.checksum
        display += "\nheader Size:\t\t %s" % self.header_size
        display += "\n"
        return display
