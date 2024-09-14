n = int(input("Digite o valor de N: "))

if n > 0:
    for i in range(1, n+1, 1):
        print(i)
        if i % 2 == 0:
            print("  > Par!")
        else:
            print("  > Ímpar!")

