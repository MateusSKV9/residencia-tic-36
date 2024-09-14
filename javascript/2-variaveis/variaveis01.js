//  VAR
console.log('=====> Usando \'var\' <=====');
var mensagem = 'Olá, Mundo';
console.log(mensagem);

//LET
console.log('=====> Usando \'let\' <=====');
let nome = 'Mateus';
if(true) {
    let nome = 'Santos';
    console.log(nome);
}
console.log(nome);

//CONST
console.log('=====> Usando \'const\' <=====');
const PI = 3.14;
console.log(PI);