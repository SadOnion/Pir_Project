class Worker:
    name=""
    surname=""
    cardID=None
    id=None
    isWorking=False
    def __init__(self, name, surname,cardId,id):
        self.id =id
        self.name=name
        self.surname=surname
        self.cardID=cardId
    def __str__(self):
        return self.name+" "+self.surname+" "+str(self.cardID)+" "+str(self.id)
    def getCard(self):
        return self.cardID