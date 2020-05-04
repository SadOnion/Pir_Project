from Server import Server
from RFIDClient import RFIDClient
import paho.mqtt.client as mqtt
import time
broker = "DESKTOP-NOGE6FP"
port=8883
server = Server()
client = mqtt.Client()


def connect_to_broker():
    client.tls_set("ca.crt")
    client.username_pw_set(username='server', password='server')
    client.connect(broker, port)
    client.on_message = process_message
    client.loop_start()
    client.subscribe("worker/name") # zmiana bo tak jest ustawione w aclfile.conf
def disconnect_from_broker():
    client.loop_stop()
    client.disconnect()
def process_message(client, userdata, message):
    message_decoded = (str(message.payload.decode("utf-8"))).split(" ")
    if message_decoded[0] != "Client":
        if server.isTerminalKnown(int(message_decoded[1])):
            print(time.ctime()+"," + message_decoded[0] + " RFID card used in terminal id:"+ message_decoded[1])
            server.addLog(int(message_decoded[0]))
        else:
            print("UNKNOWN Terminal with id:"+message_decoded[1]+" send message with RFID card:"+message_decoded[0])
    else:
        print(message_decoded[0]+ " : " +message_decoded[1])
def printMenu():
    print("0: Exit")
    print("1: Report")
def start():
    printMenu()
    connect_to_broker()
if __name__=="__main__":
    start()
    inp = input()
    while inp != "0":
        if inp == "1":
            id = input("WorkerID:")
            server.getRaport(id)
        inp=input()

