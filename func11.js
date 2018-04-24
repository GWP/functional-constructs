// func11

const Box = x => ({
    map: f => Box(f(x)),
    fold: f => f(x),
    inspect: () => `Box(${x})`
})

const LazyBox = g => ({
    map: f => LazyBox(() => f(g())),
    fold: f => f(g())
})

const nextCharForNumberString = str =>
    LazyBox(() => str)
    .map(s => s.trim())
    .map(r => parseInt(r))
    .map(i => i + 1)
    .fold(j => String.fromCharCode(j)) // if fold is not called, nothing runs



const result = nextCharForNumberString(' 64 ');

console.log(result)