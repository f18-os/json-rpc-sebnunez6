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

print("graph before increment")
root.show()
print("dictionary")
print(listToDict(root))


# do this increment remotely:
increment(root)

print("graph after increment")
root.show()
print("dictionary")
dict = listToDict(root)

# Cut-the-corners TCP Client:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 50001))

rpc = JSONRpc(s,framing_cls=JSONFramingNone)
server = rpc.get_peer_proxy()
# Execute in server:
result = server.swapper('Hello World!')
# "!dlroW olleH"
print(result)

print(server.nop(dict))

rpc.close() # Closes the socket 's' also


