This directory contains the minimal bsonrpc demos from 
https://github.com/seprich/py-bson-rpc/blob/master/README.md#quickstart 

In case you don’t understand python’s “@” decorator syntax, see
https://www.python-course.eu/python3_decorators.php

Assumptions:
Always a root
tree is never empty there is at least a root

Client:
Creates a tree. Serializes the tree using TreeToListDict and sends the
List of dictioniaries to the Server. What is retrieved from the server
will then be unserialized back into a tree. Then repeats the process
to attempt to increment in the server again

Server:
Retrieves a list of dictionaries representing a tree. Is unserialized
using ListDictToTree. The tree is then incremented. Reserialized into
a list of dictionaries using TreeToListDict and sent back to the client.

Node:
Attributes and method for tree. There is a method to create a list of
dictionaries from a tree. The method represents each node as a 
dictionary and each index represents an attribute in node. There is another
method to create a tree from a list of dictionaries recursive. It does this 
by searching for the root then creating each node associated with the root recursively.