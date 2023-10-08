class A(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return "A: a = %s, b = %s" % (self.a, self.b)

class B(A):
    def __init__(self, *args):
        if type(args[0]) is A:
            self.__dict__ = args[0].__dict__.copy()
            c = args[1]
        else:
            super(B, self).__init__(*args[:2])
            c = args[2]
        self.c = c

    def __str__(self):
        return "B: a = %s, b = %s, c = %s" % (self.a, self.b, self.c)


myA = A(1, 2)
print(myA)
print(B(3,4,5))   # regular B
myB = B(myA, 10) # B created from an A
print(myB)