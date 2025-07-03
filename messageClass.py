

class Message():
    def __init__(self, msgID, RTR, IDE, data):
        self.SOF = "SOF"
        self.msgID = msgID
        self.RTR = RTR
        self.IDE = IDE
        self.DLC = 20
        self.data = data
        self.CRC = "CRC"
        self.CRCdelimi = "!CRC"
        self.ACK = "ACK"
        self.ACKdelimit="!ACK"
        self.EOF = "EOF"