import paho.mqtt.client as mqtt
import time
import on_functions as funs #for callbacks
import generator_v3 as generator
import random



# broker = "test.mosquitto.org"
broker = "broker.hivemq.com"
#broker = "iot.eclipse.org"
#broker = "78.8.146.92:7504"    #firmowy zastepczy



if __name__ == '__main__':
    client = mqtt.Client("jursPub") #Jaroszczuk, Unold, Rudyk, Starościak
    funs.initial_config(client)
    
    client.connect(broker)
    time.sleep(3)

    client.loop_start()
    time.sleep(1)

    #simulate measurment #0
    previousMeasurment = generator.generateFirstMeasurment(random.randint(0, 2))
    while True:
        randomSensorId = random.randint(0, 2)
        payload = generator.generateMeasurment(randomSensorId, previousMeasurment)
        previousMeasurment = payload
        client.publish("jursHouse/sensor" + str(randomSensorId) + "/", payload)
        time.sleep(3)
    client.loop_stop()
    client.disconnect()

"""
HOW TO ACTIVATE VENV AND INSTALL ALL REQIREMENTS
1. `cd` to the directory where requirements.txt is located
2. activate your virtualenv
    ..\..\Environments\py38_myqsl\Scripts\activate
3. Install reqs
    pip install -r requirements.txt
"""

"""
#create new db:
CREATE TABLE nowabd (id INT(11), sensorId INT(11), pm_1_0 INT(11), pm_2_5 INT(11), pm_10 INT(11), temp DOUBLE, hum DOUBLE, time DATETIME)

#create new snakeydb:
CREATE TABLE nowabd2 (id INT(11) NOT NULL AUTO_INCREMENT,
                     sensorId INT(11) NOT NULL,
                     pm_1_0 INT(11) NOT NULL,
                     pm_2_5 INT(11) NOT NULL,
                     pm_10 INT(11) NOT NULL,
                     temp DOUBLE NOT NULL,
                     hum DOUBLE NOT NULL,
                     time DATETIME NOT NULL,
                     PRIMARY KEY (id))


#drop tables snakeydb, pet:
DROP TABLE snakeydb, pet;
"""
    





"""
# broker = "broker.mqttdashboard.com"
# port = 8000
broker = "test.mosquitto.org"   #ten dziala z metoda on_connect
port = 1883



def initial_config(_sensor):
    _sensor.on_connect = funs.on_connect
    _sensor.on_publish = funs.on_publish
    _sensor.on_message = funs.on_message
    _sensor.connect(broker, port)





if __name__ == '__main__':
    sensor = mqtt.Client(client_id="Kuba")
    initial_config(sensor)

    sensor.subscribe("KubasTopic67/#")
    sensor.publish("KubasTopic67/bulb1", "dane z sensoreczka")

    sensor.publish("house/bulb1", "on")

    

    sensor.loop_forever()
"""