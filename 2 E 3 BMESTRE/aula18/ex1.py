lista = [10,20,30,40]
lista.append(int(input("Informe um inteiro: "))) #append é uma função em que o usuário acrescenta um item no FINAL da lista 
for i in lista:
    print(i)

lista2= [10,20,30,40]
num=int(input("Infomre um inteiro: "))
lista2.insert(3,num) #insert é um comando que insere um valor em uma posição específica da lista. Precisa infromar o índice e o valor
print(lista2)