nome = "Godalfredo"
c = 6
soma = 7 + c
subtracao = 3 - 1
multiplicacao = 5*5
divisao = 30/5
exponenciacao = 3**2
resto = 5%2
maior = 3>2
menor = 5<4
maiorIgual = (9>=9)
menorIgual = (7<=7)
igual = (1==1)
diferente = (11!=12)
negacao = not (11==11)
e = (1==1 and 2==2)
ou = (3>5 or 2==2)

print("Atribuição: nome = ", nome)
print("Adição: 7 +",c,"=", soma)
print("Subtração: 3-1=", subtracao)
print("Multiplicão: 5*5=", multiplicacao)
print("Divisão: 30/5=", divisao)
print("Exponenciação: 3^2=", exponenciacao)
print("Módulo (resto de uma divisão1): resto de 5 por 2 = ", resto)
print("Maior: 3>2?", maior)
print("Menor: 5<4?", menor)
print("Maior ou igual: 9>=9?", maiorIgual)
print("Igual: 7<=7?", menorIgual)
print("Diferente: 11!=12?", diferente)
print("Negação: not(11==11)", negacao)
print("E: (1==1 and 2==2)?", e)
print("Ou: (3>5 or 2==2)? ", ou)

print("\n\n")

nomeComp = input("Qual seu nome completo? ")
idade = int(input("Qual sua idade? "))

print("Seu nome completo é", nomeComp)
print("Sua idade é", idade)