import paho.mqtt.client as mqtt
from . import settings
from . import views

def on_connect(mqtt_client, userdata, flags, rc):
  if rc == 0:
    print('Connected successfully')
    mqtt_client.subscribe('CodeJam', 1)
  else:
    print('Bad connection. Code:', rc)

def on_message(mqtt_client, userdata, msg):
  views.createRow(msg.payload)


client = mqtt.Client(client_id="ColdJam on Pancakes-01")
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(settings.MQTT_USER, settings.MQTT_PASSWORD)
client.connect(
    host=settings.MQTT_SERVER,
    port=settings.MQTT_PORT,
    keepalive=settings.MQTT_KEEPALIVE
)