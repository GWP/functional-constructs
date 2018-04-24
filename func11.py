# func11

class Box:
    def __init__(self, x):
        self.x = x
        self.map = lambda f: Box(f(x))
        self.fold = lambda f: f(x)
    
    def __repr__(self):
        return 'Box({})'.format(self.x)

# Box = lambda x: {
#     'map': lambda f: Box(f(x))
#     'fold': lambda f: f(x)
# }

# def nextCharForNumberString(st):
#     return map(lambda i: chr(i), map(lambda n: n+1, map(lambda x: int(x), map(lambda s: s.strip(), [st]))))

class LazyBox:
    def __init__(self, g):
        self.map = lambda f: LazyBox(lambda: f(g()))
        self.fold = lambda f: f(g())

def intify(x):
    print("intifying")
    return int(x)

def nextCharForNumberString(st):
    return LazyBox(lambda: st).map(lambda s: s.strip()) \
        .map(intify) \
        .map(lambda n: n+1) \
        .fold(lambda i: chr(i)) # intify will not be called if fold is commented out


result = nextCharForNumberString(' 64 ')

print(result)