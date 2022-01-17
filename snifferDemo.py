import socket
import struct
import textwrap


# VIEW README FOR EXPLANATION OF FUNCTIONS


def main():
	# make a socket to have connections with other computers
	conn = 



def ethernet_frame(data):
	dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', data[:14])
	return (get_mac_addr(dest_mac), get_mac_addr(src_mac), socket.htons(proto), data[14:])






# return formatted mac_addr i.e 00:50:3E:E4:4C:00


# return formatted mac address
"""
bytes_addr is iterable
mac address is broken into chunks, we need to format it now 
example:
00:50:3E:E4:4C:00
"""


def get_mac_addr(bytes_addr):
	# bytes_addr is iterable
	bytesString = map('{:02x}'.format, bytes_addr)
	mac_addr = ':'.join(bytesString).upper()

	return(mac_addr)







