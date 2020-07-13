import log
import pymysql
import json

def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("on_connect: OK, result code: " + str(rc))
    else:
        print("on_connect: ERROR, result code: " + str(rc))

def on_disconnect(client, userdata, flags, rc=0):
    print("on_disconnect: Device DISCONNECTED w/ rc: " + str(rc))

def on_subscribe(client, userdata, mid, granted_qos):
    print("on_subscribe: subscribe COMPLETED")

def on_publish(client, userdata, mid):
    print("on_publish: i just published")

def on_message(client, userdata, message):
    topic = message.topic
    payload = str(message.payload.decode("utf-8"))
    print("on_message: ", topic, ": ", payload, "\n")
    snakeyInsert(payload)


def snakeyInsert(payload):
    print("Using pymysql…")
    hostname = 'localhost'
    username = 'root'
    password = ''
    database = 'snakeydb'
    myConnection = pymysql.connect( host=hostname, user=username, passwd=password, db=database )
    cursor = myConnection.cursor()

    p = json.loads(payload)

    insert2 = "INSERT INTO `measurements` (`id`,`sensorId`,`pm_1_0`, `pm_2_5`, `pm_10`, `temp`, `hum`, `time`) VALUES (NULL, '" + str(p.get('sensorId')) +"', '" + str(p.get('pm_1_0')) + "', '" + str(p.get('pm_2_5')) + "', '" + str(p.get('pm_10')) + "', '" + str(p.get('temp')) + "', '" + str(p.get('hum')) + "', '" + str(p.get('time')) + "');"

    cursor.execute(insert2)

    myConnection.commit()
    myConnection.close()  


def on_log(client, userdata, level, buf):
    log.logging.debug('log: ' + buf)
    #print("log: " + buf)

def initial_config(sensor):
    sensor.on_connect = on_connect
    sensor.on_disconnect = on_disconnect
    sensor.on_subscribe = on_subscribe
    sensor.on_publish = on_publish
    sensor.on_message = on_message
    sensor.on_log = on_log
