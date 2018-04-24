# func10

class Sum:
    def __init__(self, x):
        self.x = x
        self.concat = lambda o: Sum(x + o.x)
    
    def __repr__(self):
        return 'Sum({})'.format(self.x)
    
    @staticmethod
    def empty():
        return Sum(0)