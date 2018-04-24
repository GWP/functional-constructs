# func17
import re

modulo = lambda x: lambda y: y % x

is_odd = modulo(2)

filt = lambda pred: lambda xs: filter(pred, xs)

all_odds = filt(is_odd)

# result = all_odds([1, 2, 3, 4])

replace = lambda regex: lambda repl: lambda st: re.sub(regex, repl, st)

censor = replace('[aeiou]')('*')

# result = censor('hello world')

custom_map = lambda f: lambda xs: map(f, xs)

censor_all = custom_map(censor)

result = list(censor_all(['hello', 'world']))

# print(list(result))
print(result)