n=int(input("Somar pares de 1 até: "))
soma=0
contador=1
n_for_par=n

if n%2==0:
    n-=1
    while contador<=n:
        soma+=contador
        contador+=2
    print(f"Somar pares de 1 até {n} = {soma} ")
else:
    while contador<=n:
        soma+=contador
        contador+=2
    print(f"Somar pares de 1 até {n_for_par} = {soma} ")