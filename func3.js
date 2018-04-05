// func3

// const either = Right || Left

const Box = x => ({
    map: f => Box(f(x)),
    fold: f => f(x),
    inspect: () => `Box(${x})`
})

const Right = x => ({
    map: f => Right(f(x)),
    fold: (f, g) => g(x),
    inspect: () => `Right(${x})`
})

const Left = x => ({
    map: f => Left(x),
    fold: (f, g) => f(x),
    inspect: () => `Left(${x})`    
})

const fromNullable = x =>
    x != null ? Right(x) : Left(null)

const findColor = name =>
    fromNullable({
        red: '#ff4444',
        blue: '#3b5998',
        yellow: '#fff68f'
    }[name])

// const result = Right(3).map(x => x + 1).map(x => x / 2).fold(x => 'error', x => x);
const result = findColor('red').map(r => r.slice(1)).fold(e => 'no color', 
                                                          c => c.toUpperCase());
console.log(result);