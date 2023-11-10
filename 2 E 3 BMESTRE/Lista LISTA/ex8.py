quant=int(input("Informe a quantidade de notas: "))
lista=[]
soma=0

for i in range (1,quant+1):
    nota=float(input(f"Informe a {i}° nota: "))
    lista.append(nota)
    soma+=nota
media=soma/quant

print(f"Notas: {lista}")
print(f"Média: {media}")