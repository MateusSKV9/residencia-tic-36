a = 21
b = 50
c = 21
d = 22

if b>a:
    print(b,"é maior que",a)

if c<d:
    print(c,"é menor que",d)

temperatura = int(input("\nDigite a temperatura: "))

if temperatura > 32:
    print("Dia quente")
elif temperatura >20 and temperatura <=32:
    print("Dia aggradável")
else:
    print("Dia frio")
    if temperatura<3:
        print("Com risco de neve")