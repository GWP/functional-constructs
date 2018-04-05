# func1

# // const nextCharForNumberString = str => {
# //     const trimmed = str.trim();
# //     const number = parseInt(trimmed);
# //     const nextNumber = number + 1;
# //     return String.fromCharCode(nextNumber)
# // }

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

def nextCharForNumberString(st):
    return Box(st).map(lambda s: s.strip()) \
        .map(lambda x: int(x)) \
        .map(lambda n: n+1) \
        .fold(lambda i: chr(i)) \


result = nextCharForNumberString(' 64 ')

print(result)