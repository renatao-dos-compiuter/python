inicio = int(input("Informe o valor de início: "))
fim = int(input("Informe o valor final: "))
lista=[]

for i in range(fim, inicio-1, -1):
    lista.append(i)
print(lista)