var hoje = new Date();
var data_natal = new Date(hoje.getFullYear, 11, 25);

if (hoje.getMonth() === 11 && hoje.getDate() > 25) {
    data_natal.setFullYear(hoje.getFullYear() + 1);
}

var diferenca = data_natal - hoje;

console.log(diferenca);