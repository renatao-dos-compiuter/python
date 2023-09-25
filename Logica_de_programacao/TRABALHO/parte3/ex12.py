print("Operação-Adição!")
n1=int(input("Informe um valor: "))
n2=int(input("Informe outrio valor: "))
print(f"{n1} + {n2} = {n1+n2}")
resposta=input("Deseja realizar mais uma soma? (S ou N) ")
while resposta == "S" or resposta == "s":
    print("Operação-Adição!")
    n1=int(input("Informe um valor: "))
    n2=int(input("Informe outrio valor: "))
    print(f"{n1} + {n2} = {n1+n2}")
    resposta=("Deseja realizar mais uma soma? (S ou N) ")
while resposta == "N" or resposta == "n":
    print("fim")