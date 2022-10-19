const products = [
    {name: 'cucumber', type:'vegetable'},
    {name: 'banana', type:'fruit'},
    {name: 'carrot', type:'vegetable'},
    {name: 'apple', type:'fruit'},
]

//함수정의

const fruitFilter = funtion(product) {
    return product.type === 'fruit'
}

//콜백
const fruits = products.filter(fruitFilter)

console.log(fruits)


//2 
const fruits = products.filter(functoin (product) {
    return product.type === 'fruit'
})

//3 
const fruits = products.filter((product) => product.type === 'fruit')