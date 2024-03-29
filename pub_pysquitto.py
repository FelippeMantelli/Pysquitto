import time
import random
import paho.mqtt.client as mqtt
import randomCoordinates

def on_publish(client, userdata, mid, reason_code, properties):
    try:
        userdata.remove(mid)
    except KeyError:
        print("Não foi possível publicar sua mensagem")

to_publish_list = set()
mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_publish = on_publish

mqttc.user_data_set(to_publish_list)
mqttc.connect("localhost", port=1883)
mqttc.loop_start()

while True:
    dispositivo_id = 1
    latitude = round(random.uniform(-25, -20), 5)
    longitude = round(random.uniform(-45, -40), 5)
    
    latitude = str(latitude)
    longitude = str(longitude)

    payload = f'{{\"lat\":\"{latitude}\", \"lon\":\"{longitude}\", \"id_dispositivo\":\"{dispositivo_id}\"}}'
    
    print(payload)

    msg_info = mqttc.publish("mqtt-trabalho", str(payload), qos=1)
    to_publish_list.add(msg_info.mid)

    while len(to_publish_list):
        time.sleep(30)

    msg_info.wait_for_publish()