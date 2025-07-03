
class ECU():
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.bus = None
        self.filter = []
    
    def sendMessage(self, messageId, Data):
        pass

    def receiveMessage(self):
        pass

    def addFilter(self, ID):
        if ID not in self.filter:
            self.filter.append(ID)
        else:
            pass

    

