function addCard() {
    const card = document.createElement("DIV");
    const fatherCard = document.getElementById("fatherCard");

    fatherCard.appendChild(card);

    card.classList.add("card");
    card.setAttribute("id", "teste");

    return;
}


function removeCard() {
    const card = document.getElementById("teste");
    const fatherCard = document.getElementById("fatherCard");
    fatherCard.removeChild(card);
    return;
}


function init () {
    const ancorAddCard = document.getElementById("ancorAddCard")
    const ancorRemoveCard = document.getElementById("ancorRemoveCard")

    ancorAddCard.addEventListener("click", addCard)
    ancorRemoveCard.addEventListener("click", removeCard)
}

//incializa o botão
init();