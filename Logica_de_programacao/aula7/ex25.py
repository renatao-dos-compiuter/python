#ex4: Implementar uma função que escreva no terminal os números naturais múltiplos de número informado, de 0 até outro número informado.

n1=int(input("Digite o primeiro número: "))
n2=int(input("Digite o segundo número: "))
contador=1
contador2=n1

if n2%n1==0:
    print(0)
    while n1<=n2:
        print(n1)
        n1=n1+contador2
        contador=contador+1
else:
    while n1<n2:
        print(n1)
        n1=n1+contador2
        contador=contador+1