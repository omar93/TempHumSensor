import json
import time
import read_dht
import pycom
import _thread
from mqtt import MQTTClient
import ubinascii
import hashlib
import machine

with open('config.json') as f:
    config = json.load(f)

def interval_send(t_):
    while True:
        send_value()
        time.sleep(t_)

def send_value():
    try:
        dht_T, dht_RH = read_dht.value()
        print('dht temp: ', dht_T) # one byte
        print('dht RH: ', dht_RH) # one byte
        c.publish(topic_pub,'{"Omar": {"dht temp":' + str(dht_T) +
                          ',"dht RH":' + str(dht_RH) +
                          '}}')
        print('Sensor data sent ..')

    except (NameError, ValueError, TypeError):
        print('Failed to send!')


topic_pub = 'devices/office-sens/'
topic_sub = 'devices/office-sens/control'
broker_url = 'sjolab.lnu.se'
client_name = ubinascii.hexlify(hashlib.md5(machine.unique_id()).digest()) # create a md5 hash of the pycom WLAN mac

c = MQTTClient(client_name,broker_url,user='iotlnu',password='micropython')
c.connect()

_thread.start_new_thread(interval_send,[1])
