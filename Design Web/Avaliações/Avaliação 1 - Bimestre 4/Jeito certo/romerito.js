function addCard() {
    const card = document.createElement("DIV");
    const fatherCard = document.getElementById("fatherCard");

    fatherCard.appendChild(card);

    card.classList.add("card");
    card.setAttribute("id", "teste");

    return;
}


function removeAll(){
    const div = document.getElementById("fatherCard");
    div.innerHTML = "";
}


function init () {
    const ancorAddCard = document.getElementById("ancorAddCard")
    const ancorRemoveCard = document.getElementById("ancorRemoveCard")

    ancorAddCard.addEventListener("click", addCard)
    ancorRemoveCard.addEventListener("click", removeAll)
}

//incializa o botão
init();