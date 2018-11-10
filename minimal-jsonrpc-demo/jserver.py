# minimalistic server example from 
# https://github.com/seprich/py-bson-rpc/blob/master/README.md#quickstart

import socket
from bsonrpc import JSONRpc
from bsonrpc import request, service_class
import json
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
        string = json.dumps(txt)
        filewriter = open("request.json","w")
        filewriter.write(string)
        filewriter.close()
        return txt


# Quick-and-dirty TCP Server:
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('localhost', 50001))
ss.listen(10)

while True:
    s, _ = ss.accept()
    # JSONRpc object spawns internal thread to serve the connection.
    JSONRpc(s, ServerServices(),framing_cls=JSONFramingNone)
