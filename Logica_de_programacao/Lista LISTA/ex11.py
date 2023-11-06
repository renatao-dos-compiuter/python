nome=input("Informe seu nome: ")
lista=[]
soma=0

for i in range(1,6):
    num=float(input(f"Informe o {i}° salto: "))
    soma+=num
    lista.append(num)
print(f"Atelta: {nome}")
print(f"Lista: {lista}")
print(f"Média dos saltos: {soma/5}m")