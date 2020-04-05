from Worker import Worker
import  datetime


class Server:

    workersFile = "workers.txt"
    terminalsFile = "terminals.txt"
    logsFile = "logs.txt"

    workers =[]
    terminals = []
    def isTerminalKnown(self, id):
        for i in self.terminals:
            if id == i:
                return True
        return False
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
        lastSum=0
        sum=0
        logsStringList = logs.readlines()
        for i in logsStringList:
            tempStr = i.split(" ")
            if tempStr[0] == "UNKNOWN":
                continue
            if tempStr[3] == str(workerId):
                raport.write(i)
                hourString = tempStr[5].split(":")
                if tempStr[6][0] == 'T':
                    h = int(hourString[0])*3600
                    m = int(hourString[1])*60
                    s = int(hourString[2])
                    lastSum=h+m+s
                else:
                    h=int(hourString[0])
                    m=int(hourString[1])
                    s=int(hourString[2])
                    sum+= h*3600+m*60+s-lastSum
        raport.write("Total Work Time: "+str(datetime.timedelta(seconds=sum)))
        print("report created in workerLogs.txt file")
    def __init__(self):
        self.loadWorkers()
        self.loadTerminals()
