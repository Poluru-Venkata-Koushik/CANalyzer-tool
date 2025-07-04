
class ECU():
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.bus = None
        self.filter = []
    
    def sendMessage(self, message):
        self.bus.sendmessage(message)

    def receiveMessage(self, message):
        if  message.msgID in self.filter:
            print (f'''
                Message : {message.data}
                ID : {message.msgID}
        ''')
        else:
            print ("This is not supposed to be happening, Must have been filtered in the BUS itself")
        


    def addFilter(self, ID):
        if ID not in self.filter:
            self.filter.append(ID)
        else:
            pass

    

