#ex9: Crie um programa que imprima a tabuada do número informado pelo usuário.

num=int(input("Digite o número que deseja ver a taboada: "))
contador=1

while contador<=10:
    print(f"{num} X {contador} = {num*contador}")
    contador=contador+1