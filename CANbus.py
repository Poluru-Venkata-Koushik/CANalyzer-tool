import heapq


class CANbus():
    def __init__(self):
        self.ECUs = []
        self.messages = []
    
    def registerECU(self, ecuIn):
        if ecuIn not in self.ECUs:
            self.ECUs.append(ecuIn)
            ecuIn.bus = self
        else:
            print("ECU already registered")

    def sendmessage(self, messageIn):
        heapq.heappush(self.messages, messageIn)
        print(f"Message {messageIn.msgID} sent to bus")

    def dispatchMessages(self):
        while self.messages:
            message = heapq.heappop(self.messages)
            for ecu in self.ECUs:
                if message.msgID in ecu.filter:
                    ecu.receiveMessage(message)
                else:
                    print(f"Message {message.msgID} not filtered by ECU {ecu.name}")

    def __str__(self):
        return (
            '''
                This is the canbus class.
            ''')
    
