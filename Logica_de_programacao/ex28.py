quant= int(input("Digite a quantidade de valores que você vai fazer a média aritimética: "))
contador=2
soma=0

num=int(input(f"Digite o 1º número: "))
while contador<=quant:
    num2=int(input(f"Digite o {contador}º número: "))
    soma=num+num2
    contador=contador+1
print(f"A média aritimética é {soma/quant-1:.2f}")