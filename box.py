class Box:
    def __init__(self, x):
        self.x = x
        self.chain = lambda f: f(x)
        self.map = lambda f: Box(f(x))
        self.fold = lambda f: f(x)
    
    def __repr__(self):
        return 'Box({})'.format(self.x)

    @staticmethod
    def of(x):
        return Box(x)