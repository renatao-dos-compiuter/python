n=int(input("Quantidade de produtos foram comprados: "))
contador=1
soma=0

while contador <=n:
    quant=int(input(f"Informe a quantidade do produto {contador} comprada: "))
    valor=float(input(f"Informe o valor unitário do produto {contador}: "))
    total=quant*valor
    print("-----------------------------------------")
    print(f"Valor total do produto comprado: {total:.2f}")
    print("-----------------------------------------")
    soma+=total
    contador+=1
print(f"Valor total das compras: {soma:.2f}")