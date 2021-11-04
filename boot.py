# This file is executed on every boot (including wake-boot from deepsleep)
import gc, webrepl, network
# import uos, machine, esp
# esp.osdebug(None)
# uos.dupterm(None, 1) # disable REPL on UART(0)

def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('ssid', 'password')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

do_connect()
webrepl.start()

gc.collect()
