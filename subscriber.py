import paho.mqtt.client as mqtt
import time
import on_functions as funs


# broker = "test.mosquitto.org"
broker = "broker.hivemq.com"
#broker = "iot.eclipse.org"


if __name__ == '__main__':
    client = mqtt.Client("jursSub") #Jaroszczuk, Unold, Rudyk, Starościak
    funs.initial_config(client)
    
    client.connect(broker)
    time.sleep(3)

    #client.loop_start()
    client.subscribe("jursHouse/#")
    

    #client.publish("house/sensor1/kuba/buba", "my 1st msg")
    time.sleep(4)
    client.loop_forever()

    #client.disconnect()
    