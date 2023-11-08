lista_altura=[]
lista_idade=[]

for contador in range (1,6):
    altura=float(input(f"Digite a altura da {contador}° pessoa em metros: "))
    lista_altura.insert(0,altura)
    idade=float(input(f"Digite a idade da {contador}° pessoa: "))
    lista_idade.insert(0,idade)
print(lista_altura)
print(lista_idade)