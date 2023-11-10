num= int(input('Digite a quantidade de números da lista: '))
lista=[]
contador=0

for i in range(num):
    indice=int(input(f"Informe o número do índice {contador} da lista: "))
    contador+=1
    indice*=2
    lista.append(int(indice))
print(lista)