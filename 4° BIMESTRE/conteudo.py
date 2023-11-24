# lista.sort() = DEIXA OS ITENS EM ORDEM ALFABÉTICA OU EM ORDEM CRESCENTE

# lista.sort()
# lista.reverse() = ISSO TUDO DEIXA EM ORDEM DECRESCENTE

lista_notas=[]
soma=0

quant=int(input("Informe a quantidade de notas: "))
for i in range (1,quant+1):
    nota=int(input(f"Informe a {i}º nota: "))
    lista_notas.append(nota)
    soma+=nota
lista_notas.sort()
print(f"Lista de notas: {lista_notas}")
print(f"Média= {soma/quant}")