# -*- coding: utf-8 -*-
import xmlrpclib
url = "https://server.name.com"

username = "user@roomdoo.es"
password = "PaSsWoRd"

db = "databasename"

common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
print common.version()

uid = common.authenticate(db, username, password, {})
models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))

u"""
    archivo == 0 'Todo'
    archivo == 1 'Tarifa'
    archivo == 2 'Canal'
    archivo == 3 'Hotel'
    archivo == 4 'Pais'
    archivo == 5 'Regimen'
    archivo == 6 'Reservas'
    archivo == 7 'Capacidad'
    archivo == 8 'Tipo Habitación'
    archivo == 9 'Budget'
    archivo == 10 'Bloqueos'
    archivo == 11 'Motivo Bloqueo'
    archivo == 12 'Segmentos'
    archivo == 13 'Clientes'
    archivo == 14 'Estado Reservas'
    archivo == 15 'Room names'
    fechafoto = 'Fecha a partir de la que tomar datos yyy-mm-dd'
"""


# a = models.execute_kw(db, uid, password, 'data_bi', 'export_data_bi', [ 0, '2000-01-01'])
a = models.execute_kw(db, uid, password, 'data_bi', 'export_data_bi', [ 0])

print a
