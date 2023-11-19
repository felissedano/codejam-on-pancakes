import paho.mqtt.client as mqtt
import json
import requests
import time


def on_connect(mqtt_client, userdata, flags, rc):
    if rc == 0:
        print('Connected successfully')
        mqtt_client.subscribe('CodeJam', 1)
    else:
        print('Bad connection. Code:', rc)

def on_message(mqtt_client, userdata, msg):
    jsonObj = msg.payload.decode('UTF-8')
    jsonObj = json.loads(jsonObj)
    try:
        requests.post(url="http://localhost:8000/readMsg/",json=jsonObj)
    except:
        print("RUN DJANGO PLS")

def run_client():

    client = mqtt.Client(client_id="Codejam on Pancakes-01", clean_session=True)
    client.username_pw_set("CodeJamUser", "123CodeJam")
    client.connect("fortuitous-welder.cloudmqtt.com", 1883)
    client.subscribe("CodeJam", qos=1)
    client.on_connect = on_connect
    client.on_message = on_message
    startTime = time.perf_counter()
    runTime = 20 #5 * 60
    while True:
        client.loop()
        currentTime = time.perf_counter()
        if (currentTime - startTime) > runTime:
            break