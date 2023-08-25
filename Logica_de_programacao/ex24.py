base=int(input("Digite a base da potência: "))
expoente=int(input("Digite o expoente da potência: "))
contador=1

while contador<=expoente:
    base=base*base
    contador=contador+1
print(base)