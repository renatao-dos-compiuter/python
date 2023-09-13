#ex8: Fazer um programa que lê números inteiros até que zero seja lido. Ao final mostra a soma dos números lidos.

n=int(input("Digite um número: "))
soma=0
soma=n

while n!=0:
    n=int(input("Digite um número: "))
    soma=soma+n
print("A soma é", soma)
