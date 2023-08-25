n1=int(input("Digite o primeiro número: "))
n2=int(input("Digite o segundo número: "))

if n2%n1==0:
    print(0)
    while n1<=n2:
        print(n1)
        n1=n1+n1