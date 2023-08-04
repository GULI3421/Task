class Phone:
    def __init__(self, number, model, weight):
        self.number = number
        self.model = model
        self.weight = weight

    def receiveCall(self, name):
        print("Звонит", name)

    def getNumber(self):
        return self.number

a = Phone(707234634, "mi", 150)
b = Phone(555301264, "iphone", 170)
c = Phone(770983764, "samsung", 190)

a.receiveCall("Владислав")
a.getNumber()
b.receiveCall("Алексей")
b.getNumber()
c.receiveCall("Евгений")
c.getNumber()
