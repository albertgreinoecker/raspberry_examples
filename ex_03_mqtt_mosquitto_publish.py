import paho.mqtt.client as mqtt

# Diese paar Zeilen Code reichen aus um etwas an einen Channel zu senden
client = mqtt.Client('X12') #Der Parameter ist die client-ID, diese sollte möglichst eindeutig sein.

#client.username_pw_set('albert', 'XXX')
client.connect('127.0.0.1', port=2222) #Im Moment verwenden wir die lokale mosquitto Installation, spaeter durch die IP zu ersetzen
#client.connect('os-beyond.at')

client.publish("house/light","ON")  #An den Channel house/light wird die Nachricht "ON" gesendet