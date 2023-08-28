n1=int(input("Digite o primeiro número: "))
n2=int(input("Digite o segundo número: "))
contador=1
contador2=n1

if n2%n1==0:
    print(0)
    while contador<=n2:
        print(n1)
        n1=n1+n1
        contador=contador+1