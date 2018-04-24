// func8

// Semigroup: An associative type with a concat method. 
// Monoid: A Semigroup with a neutral element (empty method)

const Sum = x => ({
    x,
    concat: ({x: y}) => Sum(x + y),
    inspect: () => `Sum(${x})`
})

Sum.empty = () => Sum(0)

// const result = Sum.empty().concat(Sum(1).concat(Sum(2))) // want Sum(3)

const All = x => ({
    x,
    concat: ({x: y}) => All(x && y),
    inspect: () => `All(${x})`
})

All.empty = () => All(true)

// const result = All(true).concat(All(false)).concat(All.empty()) // All(false)


const First = x => ({
    x,
    concat: () => First(x),
    inspect: () => `First(${x})`
})

// There is no way to define a neutral element on First, thus First remains a Semi-group and cannot be a Monoid.

// const result = First("blah").concat(First("ice cream")) // First(false)

const sum = xs =>
    xs.reduce((acc, x) => acc + x, 0)

const result = sum([1,2,3])


console.log(result)