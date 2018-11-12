# minimalistic client example from 
# https://github.com/seprich/py-bson-rpc/blob/master/README.md#quickstart

import socket
from bsonrpc import JSONRpc
from bsonrpc.exceptions import FramingError
from node import *
from bsonrpc.framing import (
	JSONFramingNetstring, JSONFramingNone, JSONFramingRFC7464)

leaf1 = node("leaf1")
leaf2 = node("leaf2")

root = node("root", [leaf1, leaf1, leaf2])


# Cut-the-corners TCP Client:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 50001))

rpc = JSONRpc(s,framing_cls=JSONFramingNone)
server = rpc.get_peer_proxy()
# Execute in server:
print("graph before increment-------------------")				#show graph before increment
root.show()
list = TreeToListDict(root)
print("\n\n")
print("graph after increment---------------------")				#show graph after increment
list = server.increment(list)
root = ListDictToTree("root",list)
root.show()
print("\n\n")
print("graph before increment-------------------")				#show graph before increment
root.show()
print("\n\n")
list = server.increment(list)
print("graph after increment---------------------")				#show graph after increment
root = ListDictToTree("root",list)
root.show()
print("\n\n")

rpc.close() # Closes the socket 's' also


