class Pessoa {
    constructor (nome, snome) {
        this.nome = nome;
        this.snome = snome;
    }

    getNome () {
        return this.nome;
    }

    getSNome () {
        return this.snome;
    }

}

function adicionarPessoa () {
    const nome = document.getElementById("nome")
    const snome = document.getElementById("snome")

    if (nome.value === "" || snome.value === "") {
        return;
    }

    const div = document.getElementById("nomes")
    const element = document.createElement("p")
    element.innerText = nome.value + " " + snome.value
    div.appendChild(element)

    nome.value = ""
    snome.value = ""
    nome.focus()

}

botao = document.getElementById("enviar")
botao.addEventListener("click", adicionarPessoa)
