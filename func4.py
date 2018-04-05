# func4
import json

class Right:
    def __init__(self, x):
        self.x = x
        self.chain = lambda f: f(x)
        self.map = lambda f: Right(f(x))
        self.fold = lambda f,g: g(x)
    
    def __repr__(self):
        return 'Right({})'.format(self.x)

class Left:
    def __init__(self, x):
        self.x = x
        self.chain = lambda f: Left(x)
        self.map = lambda f: Left(x)
        self.fold = lambda f,g: f(x)
    
    def __repr__(self):
        return 'Left({})'.format(self.x)

from_nullable = lambda x: Right(x) if x else Left(None)

def try_except(f):
    try:
        return Right(f())
    except Exception as err:
        return Left(err)


get_port = lambda: try_except(lambda: open('config.json')) \
        .chain(lambda s: try_except(lambda: json.load(s))) \
        .fold(lambda e: 3000, lambda c: c['port'])

result = get_port()

print(result)