#ex3: Faça um programa que peça dois números (base e expoente), calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.]

base=int(input("Digite a base da potência: "))
expoente=int(input("Digite o expoente da potência: "))
contador=0
potencia=1

while contador<expoente:
        potencia=potencia*base
        contador=contador+1
print(potencia)