const numbers = [1,2,3]

// 표현식 함수 정의
const doubleFunc = function (number) {
    return number * 2
}

// 함수를 다른 함수의 인자로 넣기 (콜백함수)

const doubleNumbers = numbers.map(doubleFunc)

console.log(doubleNumbers)  // [2,4,6]

//2.
const newArry = numbers.map(function (number) {
    return number*2
})

//3.
const newArry = numbers.map((number) => {
    return number*2
})

//4. 
const newArry = numbers.map((number)=> number*2)