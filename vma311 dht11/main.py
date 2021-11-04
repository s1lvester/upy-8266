import machine, time, dht

d = dht.DHT11(machine.Pin(2))

while True:
    d.measure()
    print(d.temperature(), " | ", d.humidity())
    print("------------------")
    time.sleep(5)