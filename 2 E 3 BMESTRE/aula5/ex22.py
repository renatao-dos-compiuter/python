#ex1: Faça um programa que receba dois números inteiros e imprima os números inteiros que estão no intervalo compreendido entre estes números digitados.

n1=int(input("Digite um número: "))
n2=int(input("Digite outro número: "))

if n1<n2:
    while n1<=n2:
        print(n1)
        n1=n1+1
elif n2<n1:
    while n2<=n1:
        print(n2)
        n2=n2+1