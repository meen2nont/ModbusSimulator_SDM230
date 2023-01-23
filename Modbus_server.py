from pyModbusTCP.server import ModbusServer, DataBank
from time import sleep
from random import uniform
#Create an Instance of ModbusServer
server=ModbusServer("127.0.0.1",502,no_block=True)
try:
    print("Server Starting....")
    server.start()
    print("Server is online")
    state = [0]
    while True:
        continue

except:
    server.stop()
    print("Server is stoping....")
    server.stop()
    print("Server is offline")
    