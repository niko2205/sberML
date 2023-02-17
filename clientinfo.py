# -*- coding: utf-8 -*-

from xmlrpc.server import SimpleXMLRPCServer
server = SimpleXMLRPCServer(('localhost', 9000))

deal_inn = {
    "1":"0000000051",
    "2":"0000000062",
    "3":"0000000073",
    "4":"0000000084",
    "5":"0000000095"
}

inn_fio = {
    "0000000051": "Иванов Иван Иванович",
    "0000000062": "Петров Пётр Петрович",
    "0000000073": "Сидоров Сидр Сидорович",
    "0000000084": "Смирнов Михаил Николаевич",
    "0000000095": "Павлов Павел Павлович"
}

def get_inn(deal_id):
    return deal_inn[str(deal_id)]

def get_fio(inn):
    return inn_fio[str(inn)]

server.register_function(get_inn)
server.register_function(get_fio)
server.serve_forever()