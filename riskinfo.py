# -*- coding: utf-8 -*-

from xmlrpc.server import SimpleXMLRPCServer
server = SimpleXMLRPCServer(('localhost', 9090))

inn_history = {
    "0000000051": "Хорошая",
    "0000000062": "Плохая",
    "0000000073": "Хорошая",
    "0000000084": "Плохая",
    "0000000095": "Хорошая"
}

def get_history(inn):
    return inn_history[str(inn)]

server.register_function(get_history)
server.serve_forever()