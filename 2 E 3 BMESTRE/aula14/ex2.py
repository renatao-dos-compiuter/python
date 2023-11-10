n=int(input("Infrome o número de valores: "))
soma=0
for contador in range (1,n+1):
    valor=float(input(f"Infrome o {contador}° valor: "))
    soma+=valor
media=soma/n
print(f"A média aritimética é {media:.1f}")