import paho.mqtt.client as mqtt
import uuid

# Diese paar Zeilen Code reichen aus um etwas an einen Channel zu senden

# Der Parameter ist die client-ID, diese sollte möglichst eindeutig sein.
# Falls man diesen weglässt, wird eine eindeutige ID erzeugt


# So kann man eine eindeutige ID erzeugen
uuid4 = uuid.uuid4() # zufällige UUID
uuid1 = uuid.uuid1() # UUID aus der MAC-Adresse und der Zeit
#client = mqtt.Client(uuid4)
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
#client.username_pw_set('albert', 'XXX')
client.connect('127.0.0.1', port=1883) #Im Moment verwenden wir die lokale mosquitto Installation, spaeter durch die IP zu ersetzen

client.publish("house/light","ON")  #An den Channel house/light wird die Nachricht "ON" gesendet
