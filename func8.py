# func8

# Monoid: A Semigroup with a neutral element

class Sum:
    def __init__(self, x):
        self.x = x
        self.concat = lambda o: Sum(x + o.x)
    
    def __repr__(self):
        return 'Sum({})'.format(self.x)
    
    @staticmethod
    def empty():
        return Sum(0)


# result = Sum.empty().concat(Sum(1).concat(Sum(2)))


class All:
    def __init__(self, x):
        self.x = x
        self.concat = lambda o: All(x & o.x)
    
    def __repr__(self):
        return 'All({})'.format(self.x)

    @staticmethod
    def empty():
        return All(True)


result = All(True).concat(All(False)).concat(All.empty())

class First:
    def __init__(self, x):
        self.x = x
        self.concat = lambda o: First(x)
    
    def __repr__(self):
        return 'First({})'.format(self.x)


# result = First('blah').concat(First('ice cream'))

print(result)