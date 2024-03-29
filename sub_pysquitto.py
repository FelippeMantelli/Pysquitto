import paho.mqtt.client as mqtt

def on_subscribe(client, userdata, mid, reason_code_list, properties):
    if reason_code_list[0].is_failure:
        print(f"O Broker não aceitou sua inscrição: {reason_code_list[0]}")
    else:
        print(f"O Broker te permitiu na seguinte QoS: {reason_code_list[0].value}")


def on_message(client, userdata, message):
    userdata.append(message.payload)
    print(message.payload)

def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code.is_failure:
        print(f"Falha de conexão: {reason_code}. Iniciando nova tentativa")
    else:
        client.subscribe("coordenadas/#")

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.on_subscribe = on_subscribe

mqttc.user_data_set([])
mqttc.connect("localhost")
mqttc.loop_forever()
print(f"A seguinte mensagem foi recebida: {mqttc.user_data_get()}")