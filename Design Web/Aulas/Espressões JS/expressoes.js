let p = {nome: "Romerito"}

class Pessoa {
    constructor (nome) {
        this.nome = nome
    }
}


let p2 = new Pessoa("Romerito")
console.log(p2)
console.log(typeof(p2))
console.log(p instanceof Pessoa)
