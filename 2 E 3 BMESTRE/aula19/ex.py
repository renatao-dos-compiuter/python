resposta="S"
lista=[]

while resposta=="S":
    n1=(int(input("Infrome um número: ")))
    n2=(int(input("Infrome outro número: ")))
    soma=n1+n2
    lista.append(soma)
    resposta=input("Deseja realizar outra operação? [S/N] ")
print(f"Resultados: {lista}")