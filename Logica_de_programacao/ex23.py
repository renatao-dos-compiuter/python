contador=1
par=0
impar=0

while contador<=10:
    n=int(input(f"Digite o {contador}º número: "))
    if n%2==0:
        par=par+1
        contador=contador+1
    elif n%2!=0:
        impar=impar+1
        contador=contador+1
print(f"Números pares: {par}")
print(f"Números ímpares: {impar}")