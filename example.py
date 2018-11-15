from binascii import unhexlify
from pprint import pprint

from sflow import decode


# Example datagram taken from http://packetlife.net/captures/protocol/sflow/

raw = '0000000500000001ac15231100000001000001a6673f36a00000000100000002' +\
      '0000006c000021280000040c0000000100000001000000580000040c00000006' +\
      '0000000005f5e100000000010000000300000000018c6e9400009b9e00029062' +\
      '0001f6c400000000000000000000000000000000005380600000a0de0000218a' +\
      '000008d7000000000000000000000000'

data = unhexlify(raw)

pprint(decode(data))