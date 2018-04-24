// func6

// Semigroup: An associative type with a concat method. 

const Sum = x => ({
    x,
    concat: ({x: y}) => Sum(x + y),
    inspect: () => `Sum(${x})`
})

// const result = Sum(1).concat(Sum(2)) // want Sum(3)

const All = x => ({
    x,
    concat: ({x: y}) => All(x && y),
    inspect: () => `All(${x})`
})


// const result = All(true).concat(All(true)) // All(false)


const First = x => ({
    x,
    concat: () => First(x),
    inspect: () => `First(${x})`
})


const result = First("blah").concat(First("ice cream")) // First(false)

console.log(result)