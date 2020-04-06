from Worker import Worker
import  datetime


class Server:

    workersFile = "workers.txt"
    terminalsFile = "terminals.txt"
    logsFile = "logs.txt"

    workers =[]
    terminals = []

    def loadWorkers(self):
        workersDB = open(self.workersFile, "r")
        workersStringList = workersDB.readlines()
        for i in workersStringList:
            tempStr = i.split(" ")
            self.workers.append(Worker(tempStr[0], tempStr[1], int(tempStr[2]), int(tempStr[3])))
    def loadTerminals(self):
        terminalsDB = open(self.terminalsFile, "r")
        workersStringList = terminalsDB.readlines()
        for i in workersStringList:
            self.terminals.append(int(i))
    def addLog(self,cardId):
         worker = self.getWorker(cardId)
         logs = open(self.logsFile, "a")
         if worker == None:
             log = "UNKNOWN" + " " + datetime.datetime.strftime(datetime.datetime.now(),"%x") + " " + datetime.datetime.strftime(datetime.datetime.now(), "%X")+ "\n"
         else:
            worker.isWorking= not worker.isWorking
            log = str(worker) + " " + datetime.datetime.strftime(datetime.datetime.now(),"%x")+" "+datetime.datetime.strftime(datetime.datetime.now(),"%X")+" "+str(worker.isWorking)+"\n"
         logs.write(log)
    def getWorker(self,cardId):
        for i in range(len(self.workers)):
            if self.workers[i].cardID == cardId:
                return self.workers[i]
        return None
    def getRaport(self,workerId):
        logs = open(self.logsFile, "r")
        raport= open("workerLogs.txt","w")
        hour=0
        min=0
        sec=0
        h = 0
        m = 0
        s = 0
        logsStringList = logs.readlines()
        for i in logsStringList:
            tempStr = i.split(" ")
            if tempStr[3] == str(workerId):
                raport.write(i)
                hourString = tempStr[5].split(":")
                if tempStr[6][0] == 'T':
                    h = int(hourString[0])
                    m = int(hourString[1])
                    s = int(hourString[2])
                else:
                    hour+=int(hourString[0])-h
                    min+=int(hourString[1])-m
                    sec+=int(hourString[2])-s

        raport.write("Total Work Time: "+str(hour)+":"+str(min)+":"+str(sec))
    def __init__(self):
        self.loadWorkers()
