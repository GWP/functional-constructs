# func3

from collections import defaultdict

class Box:
    def __init__(self, x):
        self.x = x
        self.map = lambda f: Box(f(x))
        self.fold = lambda f: f(x)
    
    def __repr__(self):
        return 'Box({})'.format(self.x)

class Right:
    def __init__(self, x):
        self.x = x
        self.map = lambda f: Right(f(x))
        self.fold = lambda f,g: g(x)
    
    def __repr__(self):
        return 'Right({})'.format(self.x)

class Left:
    def __init__(self, x):
        self.x = x
        self.map = lambda f: Left(x)
        self.fold = lambda f,g: f(x)
    
    def __repr__(self):
        return 'Left({})'.format(self.x)

# const fromNullable = x =>
#     x != null ? Right(x) : Left(null)

from_nullable = lambda x: Right(x) if x else Left(None)

def findColor(name):
    return from_nullable(defaultdict(lambda: None, {
        'red': '#ff4444',
        'blue': '#3b5998',
        'yellow': '#fff68f'
    })[name])

result = findColor('red').map(lambda x: x[1:]).fold(lambda e: 'no color', lambda x: x.upper())

print(result)