class calc:
    def __init__(s,a,b):
        s.a=a
        s.b=b
    def add(s):
        return s.a+s.b
    @classmethod
    def input(cls):
        a=int(input("Enter number"))
        b=int(input("Enter number"))
        return cls(a,b)
    @staticmethod
    def mul(x,y):
        return x*y
c=calc.input()
print("Addition-instance",c.add())
x=int(input("Enter a number for multiplication:"))
y=int(input("Enter a number :"))
print("Multiplication - static",calc.mul(x,y))