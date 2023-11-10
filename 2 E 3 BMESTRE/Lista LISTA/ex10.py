lista=[]
soma=0
multiplicacao=1

quant=int(input("Informe a quantidade de números da lista: "))

for i in range (1,quant+1):
    numero=int(input(f"Informe o {i}° número: "))
    lista.append(numero)
    soma+=numero
    multiplicacao*=numero
print(f"A lista é: {lista}")
print(f"A soma é {soma}")
print(f"A multiplicação é {multiplicacao}")