total =  float(input("Digite o valor da conta: "))
pessoas = 4

while pessoas>0:
    print("Pessoa ",(5-pessoas),": ")
    valor = float(input("\tValor: "))
    total -= valor;
    print("Restante: ", total)
    pessoas-=1

print("Conta paga!")

