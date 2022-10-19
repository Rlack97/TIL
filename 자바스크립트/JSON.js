const jsonData = {
    coffee:'Americano',
    dessert:'macaron',
    iceCream: 'Mint Choco',
}

//object -> json
const objToJson = JSON.stringify(jsonData)

//json -> object
const jsonToObj = JSON.parse(objToJson)
