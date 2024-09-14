n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
n3 = int(input("Digite um número: "))

if(n1>n2):
    aux = n1
    n1 = n2
    n2 = aux

if(n1>n3):
    aux = n1
    n1 = n3
    n3 = aux

if(n2>n3):
    aux = n2
    n2 = n3
    n3 = aux

print("Números em ordem crescente: ", n1, n2, n3)