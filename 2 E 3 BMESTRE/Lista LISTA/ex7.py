tabuada=int(input("Informe um número para a Tabuada: "))
lista=[]

for i in range(1,11):
    multiplicacao= i*tabuada
    lista.append(multiplicacao)
print(lista)