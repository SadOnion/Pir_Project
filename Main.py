from Server import Server
from RFIDClient import RFIDClient

def printMenu():
    print("0: Exit")
    print("1: Read")
    print("2: Report")
if __name__=="__main__":
    srv=Server()
    terminal=RFIDClient(1)
    printMenu()
    inp = input()
    while inp != "0":
        if(inp == "1"):
            cardId = terminal.rfidRead(4627356735619)
            srv.addLog(cardId)
        if inp == "2":
            id = input("WorkerID:")
            srv.getRaport(id)
        inp=input()

