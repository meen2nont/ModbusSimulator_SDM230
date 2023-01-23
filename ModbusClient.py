from pyModbusTCP.client import ModbusClient
client = ModbusClient(host="127.0.0.1",port=502)
status=client.open()
print(status)
i=0
while status is True:
    for i in range(99):
        client.write_single_register(0,17255)
        client.write_single_register(1,11433)
        client.write_single_register(6,16295)
        client.write_single_register(7,11453)
        client.write_single_register(12,17226)
        client.write_single_register(13,5376)
        client.write_single_register(18,17251)
        client.write_single_register(19,12456)
        client.write_single_register(24,49871)
        client.write_single_register(25,43340)
        client.write_single_register(30,16227)
        client.write_single_register(31,37660)
        client.write_single_register(36,17318)
        client.write_single_register(37,24290)
        client.write_single_register(71,16967)
        client.write_single_register(72,52748)
        # print(client.read_holding_register(i))
        print("Holding register(%s) = %s" %(i,client.read_holding_registers(i)))
        i=i+1
else:
    print("Mobus server not connected!")
