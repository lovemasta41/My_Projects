class upperstring:
    def __init__(self):
        self.s = ""
    def getstring(self):
        self.s = input("Provide String:")        
    def printstring(self):
        take = self.s
        l= take.upper()
        print(l)


strObj = upperstring()
strObj.getstring()
strObj.printstring()

