class Calculator:
    def __init__(self):
        self.one = 1
        self.two = 2
        self. three = 3
        self.four = 4
        self.five = 5

    def setdata1(self):
        self.one = 1
        self.two = 2
        self. three = 3
        self.four = 4
        self.five = 5

    def setdata2(self):
        self.one = 6
        self.two = 7
        self.three = 8
        self.four = 9
        self.five = 10

    def sum(self):
        result = self.one + self.two + self.three + self.four + self.five
        return result

    def avg(self):
        result = (self.one + self.two + self.three + self.four + self.five)/5
        return result

cal1 = Calculator()
cal2 = Calculator()

cal1.setdata1()
cal2.setdata2()
print(cal1.sum())
print(cal1.avg())
print(cal2.sum())
print(cal2.avg())