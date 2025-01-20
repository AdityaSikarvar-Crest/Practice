
class Computer:
    ram=2.5
    def __init__(self,cpu):
        self.cpu=cpu
    def config (self) :
        print ("Config is",self.cpu,self.ram)
    @classmethod
    def getram(self):
        pass
    @staticmethod
    def info():
        print("This is a computer class")
com1=Computer(2)
com2=Computer(4)
com1.info()
com1.getram()
com1.config()
com2.config()