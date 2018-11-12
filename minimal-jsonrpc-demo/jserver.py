# minimalistic server example from 
# https://github.com/seprich/py-bson-rpc/blob/master/README.md#quickstart

import socket
from bsonrpc import JSONRpc
from bsonrpc import request, service_class
import json
from node import *
from bsonrpc.exceptions import FramingError
from bsonrpc.framing import (
	JSONFramingNetstring, JSONFramingNone, JSONFramingRFC7464)


# Class providing functions for the client to use:
@service_class
class ServerServices(object):

    @request
    def swapper(self, txt):
        return ''.join(list(txt))
        
    @request
    def nop(self, txt):
        root = ListDictToTree("root",txt) #returns it back into a tree
        increment(root)                   #increments tree
        root.show()                       #prints results
        txt = TreeToListDict(root)
        return txt


# Quick-and-dirty TCP Server:
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('localhost', 50001))
ss.listen(10)

while True:
    s, _ = ss.accept()
    # JSONRpc object spawns internal thread to serve the connection.
    JSONRpc(s, ServerServices(),framing_cls=JSONFramingNone)
