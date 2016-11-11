import random
import time
from Utils.globals import version_number, latest_known_block
from Utils.dataTypes import *


class EncodeVersion:
    def __init__(self, agent):
        self.command_name = "version"

        self.version = to_int32(version_number)
        self.services = to_uint64(0)
        self.timestamp = to_int64(int(time.time()))

        self.addr_recv_services = to_uint64(0)
        self.addr_recv_ip = to_big_endian_16char(b"127.0.0.1")
        self.addr_recv_port = to_big_endian_uint16(8333)

        self.addr_trans_services = to_uint64(0)
        self.addr_trans_ip = to_big_endian_16char(b"127.0.0.1")
        self.addr_trans_port = to_big_endian_uint16(8333)

        self.nonce = to_uint64(random.getrandbits(64))
        self.user_agent_bytes = to_compactSize_uint(len(agent))
        self.user_agent = to_chars(str.encode(agent))
        self.starting_height = to_int32(latest_known_block)
        self.relay = to_bool(False)

    def forge(self):

        return self.version + self.services + self.timestamp + \
               self.addr_recv_services + self.addr_recv_ip + self.addr_recv_port + \
               self.addr_trans_services + self.addr_trans_ip + self.addr_trans_port + \
               self.nonce + self.user_agent_bytes + self.user_agent + self.starting_height + \
               self.relay


    def get_decoded_info(self):
        display = "\n-----Version-----"
        display += "\nversion                :\t\t %s" % self.version
        display += "\nservices  	         :\t\t %s" % self.services
        display += "\ntimestamp              :\t\t %s" % self.timestamp

        display += "\naddr_recv_services	 :\t\t %s" % self.addr_recv_services
        display += "\naddr_recv_ip           :\t\t %s" % self.addr_recv_ip
        display += "\naddr_recv_port         :\t\t %s" % self.addr_recv_port

        display += "\naddr_trans_services  	:\t\t %s" % self.addr_trans_services
        display += "\naddr_trans_ip         :\t\t %s" % self.addr_trans_ip
        display += "\naddr_trans_port	    :\t\t %s" % self.addr_trans_port

        display += "\nnonce                 :\t\t %s" % self.nonce

        display += "\nuser_agent_bytes  	:\t\t %s" % self.user_agent_bytes
        display += "\nuser_agent            :\t\t %s" % self.user_agent
        display += "\nstarting_height	    :\t\t %s" % self.starting_height
        display += "\nrelay	                :\t\t %s" % self.relay

        return display


class DecodeVersion:
    def __init__(self, payload):
        self.version = read_int32(payload.read(4))
        self.services = read_uint64(payload.read(8))
        self.timestamp = read_int64(payload.read(8))

        self.addr_recv_services = read_uint64(payload.read(8))
        self.addr_recv_ip = parse_ip(payload.read(16))
        self.addr_recv_port = read_big_endian_uint16(payload.read(2))

        self.addr_trans_services = read_uint64(payload.read(8))
        self.addr_trans_ip = parse_ip(payload.read(16))
        self.addr_trans_port = read_big_endian_uint16(payload.read(2))

        self.nonce = read_uint64(payload.read(8))

        self.user_agent_bytes = read_compactSize_uint(payload)
        self.user_agent = read_chars(payload.read(self.user_agent_bytes), self.user_agent_bytes)

        self.starting_height = read_int32(payload.read(4))
        self.relay = read_bool(payload.read(1))

    def get_decoded_info(self):
        display = "\n-----Version-----"
        display += "\nversion                :\t\t %s" % self.version
        display += "\nservices  	         :\t\t %s" % self.services
        display += "\ntimestamp              :\t\t %s" % self.timestamp

        display += "\naddr_recv_services	 :\t\t %s" % self.addr_recv_services
        display += "\naddr_recv_ip           :\t\t %s" % self.addr_recv_ip
        display += "\naddr_recv_port         :\t\t %s" % self.addr_recv_port

        display += "\naddr_trans_services  	:\t\t %s" % self.addr_trans_services
        display += "\naddr_trans_ip         :\t\t %s" % self.addr_trans_ip
        display += "\naddr_trans_port	    :\t\t %s" % self.addr_trans_port

        display += "\nnonce                 :\t\t %s" % self.nonce

        display += "\nuser_agent_bytes  	:\t\t %s" % self.user_agent_bytes
        display += "\nuser_agent            :\t\t %s" % self.user_agent
        display += "\nstarting_height	    :\t\t %s" % self.starting_height
        display += "\nrelay	                :\t\t %s" % self.relay

        return display
