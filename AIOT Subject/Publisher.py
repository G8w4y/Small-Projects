def on_publish(client, userdata, mid):
    print("client = " + str(client))
    print("userdata = " + str(userdata))
    print("mid = " + str(mid))
    publish()
    #client.disconnect()

def on_connect(client, userdata, flags, rc):
    print("Client: " + str(client))
    print("Userdata: " + str(userdata))
    print("Connected with result code "+str(rc))
    print("Flags: " + str(flags))
    #client.publish("Sensor/Temp", "I AM GROOT", 2)
    publish() 

def publish():
    valueTopic = input("enter topic: ")
    valuePayload = input("enter payload: ")
    client.publish(valueTopic, valuePayload)



client = mqtt.Client("Example")
client.on_connect = on_connect
client.on_publish = on_publish
client.connect("mqtt.eclipseprojects.io")
client.loop_forever()