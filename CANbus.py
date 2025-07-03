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
            pass


