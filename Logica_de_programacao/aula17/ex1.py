base=int(input("Informe a base da potência: "))
exp=int(input("Informe o expoente da potência: "))
potencia=1

for cont in range (1,exp+1):
    potencia*=base
print(potencia)