salario = float(input("Salário: "))

if(salario*12>28559.70):
    print("Você precisa declarar imposto de renda!")

    dependentes = float(input("Pendentes: "))
    pensaoAlim = float(input("Pensão alimentícia: "))
    inss = float(input("INSS: "))
    aliquota = float(input("Aliquóta: "))
    parcela_Dedutivel = float(input("Parcela Dedutível: "))

    imposto_Renda = ((salario - dependentes - pensaoAlim - inss) * aliquota) - parcela_Dedutivel
    print("Total a declarar: {}".format(imposto_Renda))
else:
    print("Você não precisa declarar imposto de renda!")

