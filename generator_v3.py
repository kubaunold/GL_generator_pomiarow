import json
import datetime
import random

def generateFirstMeasurment(sensorId):
    pm_1_0 = 0#random.randint(1, 10)  #the smallest number
    pm_2_5 = 0#random.randint(1, 25) + pm_1_0
    pm_10 = 0#random.randint(1, 100) + pm_2_5
    temp = round(random.uniform(15, 15), 2)  #returns random float
    hum = round(random.uniform(15, 15), 2)
    currentTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") #this type will be accepted by the db

    dict = {"sensorId": sensorId, "pm_1_0": pm_1_0, "pm_2_5": pm_2_5, "pm_10": pm_10, "temp": temp, "hum": hum, "time": currentTime}

    return json.dumps(dict, indent=4, sort_keys=True, default=str)  #needed for date serialization

def generateMeasurment(sensorId, previousMeasurmentJson):
    pM = json.loads(previousMeasurmentJson)

    pm_1_0 = pM.get('pm_1_0') + random.randint(-1, 2)
    pm_2_5 = pM.get('pm_2_5') + random.randint(-2, 8)
    pm_10 = pM.get('pm_10') + random.randint(-3, 13)
    temp = round(pM.get('temp') + random.uniform(-0.5, 4), 2)
    # temp = round(pM.get('temp'), 2)

    hum = round(pM.get('hum') +random.uniform(-1, 3), 2)
    currentTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") #this type will be accepted by the db
    
    dict = {"sensorId": sensorId, "pm_1_0": pm_1_0, "pm_2_5": pm_2_5, "pm_10": pm_10, "temp": temp, "hum": hum, "time": currentTime}
    return json.dumps(dict, indent=4, sort_keys=True, default=str)  #needed for date serialization
