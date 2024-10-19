setTimeout(function() {
    console.log('Essa mensagem aparece após 3 segundos');
}, 3000);

setTimeout(function(){
    console.log('Já essa aparece depois de 5 segundos');
}, 5000);

let numeros = [1, 2, 3, 4, 5];

let soma = numeros.reduce(function(acumulador, numero) {
    return acumulador+numero;
}, 0);
console.log(soma);