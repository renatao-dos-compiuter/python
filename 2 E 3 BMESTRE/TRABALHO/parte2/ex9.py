n=int(input("Somar pares de 1 até: "))
soma=0
contador=0
n_for_impar=n

if n%2==0:
    while contador<=n:
        soma+=contador
        contador+=2
    print(f"Somar pares de 1 até {n} = {soma} ")
else:
    n-=1
    while contador<=n:
        soma+=contador
        contador+=2
    print(f"Somar pares de 1 até {n_for_impar} = {soma} ")