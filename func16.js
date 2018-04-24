// func16

// Monad: type with an 'of' and a 'chain' method
// Map can be defined using chain: M.f = f => M.of(f), thus a monad is a functor

// Box, Task, Either, List

const Box = x => ({
    map: f => Box(f(x)),
    fold: f => f(x),
    inspect: () => `Box(${x})`
})

// httpGet('/user')
// .chain(user => httpGet(`/comments/${user.id}`))
// .chain(comments => updateDom(user, comments))

const join = m =>
    m.fold(x => x)


const m = Box('wonder')
// join(m.map(join)) == join(join(m))

const result = join(m.map(Box.of))

console.log(result)