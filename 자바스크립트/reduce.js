const numbers = [90,90,80,77]

const sum = tests.reduce(function(totla,x) {
    return total + x
}, 0)
// 0은 생략 가능

// 화살표 함수
const sum = tests.reduce((totla,x) => total + x, 0)

//평균
const sum = tests.reduce((totla,x) => total + x, 0) / tests.length