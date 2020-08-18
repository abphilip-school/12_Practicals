class Number(object):
    def __init__(self, x):
        self.x = x
    def __add__(self, y):
        res = float(self.x) + y
        return res
    def __sub__(self, y):
        res = float(self.x) - y
        return res
    def __mul__(self, y):
        res = float(self.x) * y
        return res

    def __div__(self, y):
        res = float(self.x) / y
        return res


num1 = int(raw_input("Enter the first number: "))
num2 = int(raw_input("Enter the second number: "))
a = Number(num1)
# format gives the values at the blank spaces
print "{} + {} = {}".format(num1, num2, a+num2)
print "{} - {} = {}".format(num1, num2, a-num2)
print "{} * {} = {}".format(num1, num2, a*num2)
print "{} / {} = {}".format(num1, num2, a/num2)
