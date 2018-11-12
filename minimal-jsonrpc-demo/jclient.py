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
print("graph before increment")				#show graph before increment
root.show()
list = TreeToListDict(root)
print("graph after passing it to the server") #test increment 1 time
list = server.nop(list)
print(list)
root = ListDictToTree("root",list)
root.show()
print("graph before increment")				#show graph before increment
root.show()
list = TreeToListDict(root)
print("graph after passing it to the server") #test increment 2 time
list = server.nop(list)
print(list)
root = ListDictToTree("root",list)
root.show()

rpc.close() # Closes the socket 's' also


