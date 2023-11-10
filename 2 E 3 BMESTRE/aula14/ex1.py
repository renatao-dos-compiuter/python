par=0
impar=0
for contador in range (1,11):
    n = int(input(f"Infrome o {contador}° valor: "))
    if n %2==0:
        par+=1
    else:
        impar+=1
print(f"Pares: {par}, ímpares {impar}")