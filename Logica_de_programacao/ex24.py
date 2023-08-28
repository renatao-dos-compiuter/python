base=int(input("Digite a base da potência: "))
expoente=int(input("Digite o expoente da potência: "))
contador=0
resultado=0

while contador<=expoente:
    resultado=resultado+base*base
    contador=contador+1
print(resultado)