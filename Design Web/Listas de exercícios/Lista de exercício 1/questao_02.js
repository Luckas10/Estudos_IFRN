palavra = "w3resource";
tamaho_palavra = palavra.length;
palavra_rotacionada = "";

for (i = tamaho_palavra - 1; i >= 0; i--) {
    palavra_rotacionada += palavra[i];
}

console.log(palavra_rotacionada);