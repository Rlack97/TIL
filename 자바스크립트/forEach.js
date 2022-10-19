const colors = ['red','blue','green']

printFunc = funtion (color) {
  console.log(color)
}

colors.forEach(printFunc)


//2.

colors.forEach(funtion (color) {
    console.log(color)
}) 

//3. 

colors.forEach ((color) => {
    console.log(color)
})