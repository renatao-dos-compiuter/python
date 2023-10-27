lista=[]
lista_par=[]
lista_impar=[]

quant=int(input("Informe a quantidade de números a serem digitadas: "))

for i in range(1,quant+1):
    numero=int(input(f"Informe o {i}° número: "))
    if numero%2==0:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)
    lista.append(numero)
print(f"Números informados: {lista}")
print(f"Números pares: {lista_par}")
print(f"Números ímpares: {lista_impar}")