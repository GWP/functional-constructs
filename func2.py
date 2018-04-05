# func2

class Box:
    def __init__(self, x):
        self.x = x
        self.map = lambda f: Box(f(x))
        self.fold = lambda f: f(x)
    
    def __repr__(self):
        return 'Box({})'.format(self.x)


def money_to_float(cost):
    return Box(cost) \
        .map(lambda s: s.replace("$", "")) \
        .map(lambda t: float(t))

def percent_to_float(discount):
    return Box(discount) \
        .map(lambda s: s.replace("%", "")) \
        .map(lambda t: float(t)) \
        .map(lambda number: number * 0.01)

def applyDiscount(price, discount):
    return money_to_float(price) \
        .fold(lambda cost: percent_to_float(discount).fold(lambda savings: cost - cost * savings))

result = applyDiscount('$5.00', '20%')

# print("cost is: {}".format(money_to_float('$5.00')))
# print("discount is: {}".format(percent_to_float('20%')))

print(result)
