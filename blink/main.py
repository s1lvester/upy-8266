import machine, time

p16 = machine.Pin(16, machine.Pin.OUT, value=1)

while True:
    if p16.value() == 0:
        p16.on()
    else:
        p16.off()

    time.sleep(1)

