class Calculator:
    def __init__(self):
        self.value

    def add(self, val):
        self.value += val

class MaxLimitCalculator(Calculator):


cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)