class Calculator:
    num = 10
    def __init__(self, a, b):
        print("into init")
        self.num1 = a
        self.num2 = b

    def getdata(self):
        print("into get data function")

    def Summation(self):
        return self.num1 + self.num2 + self.num


obj = Calculator(3, 4)
obj.getdata()
print(obj.Summation())

obj1 = Calculator(5, 4)
print(obj1.Summation())
