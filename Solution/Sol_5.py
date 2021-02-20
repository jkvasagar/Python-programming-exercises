class myString:

    def __init__(self):
        self.vStore = None

    def GetString(self):
        self.vStore = input()

    def PutString(self):
        print(self.vStore)
