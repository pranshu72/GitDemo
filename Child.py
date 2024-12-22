from FirstDemo import Calculator


class Child(Calculator):
    num3 = 20

    def __init__(self):
        Calculator.__init__(self, 2, 10)

    def getCompleteData(self):
        return self.num3 + self.num + self.Summation()


obj2 = Child()
print(obj2.getCompleteData())
