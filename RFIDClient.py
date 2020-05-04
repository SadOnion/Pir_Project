
import random
import paho.mqtt.client as mqtt
class RFIDClient:

    broker = "DESKTOP-NOGE6FP"
    port=8883
    client = None
    uidLen=5
    id=0

    def __init__(self,id):
        self.id =id
        self.client = mqtt.Client()
        self.connectToBroker()
    def connectToBroker(self):
        self.client.tls_set("ca.crt")
        self.client.username_pw_set(username='client', password='client')
        self.client.connect(self.broker, self.port)
        self.sendMessage("Client connected")
    def disconnectFromBroker(self):
        self.sendMessage("Client disconnected")
        self.client.disconnect()
    def rfidRead(self, cardId=None):
        if cardId == None:
            uid=[]
            for i in range(self.uidLen):
                rand = random.randrange(0,1000)
                uid.append(rand)
            num = 0
            for i in range(len(uid)):
                num += uid[i] << (i*8)
        else:
            num = cardId
        self.sendCardId(num)
    def sendMessage(self, msg):
        self.client.publish("worker/name",msg)
        print("msg sent")
    def sendCardId(self, cardId):
        self.client.publish("worker/name",str(cardId)+" "+str(self.id))
        print("msg sent")
if __name__ == "__main__":
    inp = input("Enter this terminal id:")
    terminal = RFIDClient(int(inp))
    print("Enter cardId to simulate rfidRead. 0 to exit. -1 to random cardId")
    inp = input()
    while inp != "0":
        if inp == "-1":
            terminal.rfidRead()
        else:
            terminal.rfidRead(int(inp))
        inp = input()
    terminal.disconnectFromBroker()
