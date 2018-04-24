// func10

const { Map, List } = require('immutable-ext')

const Sum = x => ({
    x,
    concat: ({x: y}) => Sum(x + y),
    inspect: () => `Sum(${x})`
})

Sum.empty = () => Sum(0)

// const result = List.of(Sum(1), Sum(2), Sum(3))
//                 .fold(Sum.empty())


// const result = Map({brian: 3, sara: 5}).map(Sum).fold(Sum.empty())
const result = Map({brian: 3, sara: 5}).foldMap(Sum, Sum.empty())

console.log(result)