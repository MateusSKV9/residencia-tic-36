let pessoa = {
    nome: 'Mateus',
    idade: 20,
    saudacao: function () {
        return `Olá, meu nome é ${this.nome}.`;
    }
};

console.log(pessoa);
console.log(pessoa.nome);
console.log(pessoa.idade);
console.log(pessoa.saudacao());