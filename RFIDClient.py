
import random

class RFIDClient:

    uidLen=5
    id=0

    def __init__(self,id):
        self.id =id

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
        return  num




