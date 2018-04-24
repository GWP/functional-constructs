// func17

const add = x => (y => x + y)

const inc = add(1)

// const result = inc(2)

const modulo = dvr => dvd => dvd % dvr

const isOdd = modulo(2)

const filter = pred => xs => xs.filter(pred)

const allOdds = filter(isOdd)

// const result = allOdds([1, 2, 3, 4])

const replace = regex => repl => str =>
    str.replace(regex, repl)

const censor = replace(/[aeiou]/ig)('*')

// const result = censor('hello world')

const map = f => xs => xs.map(f)

const censorAll = map(censor)

const result = censorAll(['Hello', 'World'])

console.log(result)


