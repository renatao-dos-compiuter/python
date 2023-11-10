#ex7: Faça um programa que calcule a média aritmética de n valores fornecidos pelo usuário.

quant= int(input("Digite a quantidade de valores que você vai fazer a média aritimética: "))
contador=1
soma=0

while contador<=quant:
    num=float(input(f"Digite o {contador}º número: "))
    soma=soma+num
    contador=contador+1
print(f"A média aritimética é {soma/quant:.2f}")