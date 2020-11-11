function botao(){

    document.getElementById("agradecimento").innerHTML = "Obrigado por clicar";
    //console.log(document.getElementById("agradecimento"));
    //alert("Obrigado por clicar!");
}

console.log (botao);

function redirecionar(){
    window.open("https://youtube.com");
}

/* Idade exemplo
function soma (n1, n2){
    return n1 + n2;
}

var validar = 0;
function validaIdade(idade){
    validar;
    if (idade >= 18){
        validar = true
    }else{
        validar = false
    }
    return validar;
}

var idade = prompt ("Qual a sua idade?");
validaIdade(idade)
console.log (validar);

console.log(soma(5, 10));

//alert (soma(5,10));
//console.log(soma);

*/

/* Data exemplo
var d = new Date();
console.log ("Hoje é" + d.getMonth() )
*/

/* Contar exemplo
var count;
for (count=0; count <=5; count++){
    alert(count);
    console.log(count);
}
*/

/* Contar exemplo (2)
var count = 0;
while (count < 5){
    console.log (count);
    count++;
}
*/

/* Idade exemplo (2)
var idade = prompt("Qual a sua idade?");
if (idade >= 18){
    alert("maior de idade");
} else{
    alert("menor de idade");
}
    console.log(idade);
/*

/*
var frutas = [{nome:"maçã", cor:"vermelha"},
{nome:"laranja", cor:"alaranjado"}];
console.log(frutas);
alert(frutas[1].cor);
*/

/* Lista exemplo
var lista=["maçã", "pera", "laranja"];

lista.push("uva");
lista.pop();
console.log(lista[0]);
console.log(lista,toString()[0]);

var nome = "Max";
var idade= 10;
var idade2= 29;
var JOJO = "Jojo é um bom anime";
alert(Nome + " tem" + " idade2" + " anos.");
alert(idade + idade2);
console.log(nome);
console.log (idade1 * idade2);
console.log(JOJO.toLowerCase);
alert(JOJO.replace ("bom", "ótimo"));
*/