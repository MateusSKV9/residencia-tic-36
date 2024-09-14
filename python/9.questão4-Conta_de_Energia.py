qtdKWH = float(input("Digite a quantidade de kW/h): "))

precoTotalC = qtdKWH*0.56
geracao = qtdKWH*0.41
imposto = qtdKWH*0.2252

bandeira = input("Digite a bandeira(amarela, vermelha1, vermelha2): ")
if(bandeira=="amarela" or bandeira=="Amarela"):
    valorBandeira = qtdKWH * 0.015
elif(bandeira=="vermelha1" or bandeira=="Vermelha1"):
    valorBandeira = qtdKWH * 0.040
elif(bandeira=="vermelha2" or bandeira=="Vermelha2"):
    valorBandeira = qtdKWH * 0.060

contaEnergia = precoTotalC + geracao + imposto + valorBandeira

print("Conta de energia: ", contaEnergia)