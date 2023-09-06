n=int(input("Informe um número: "))
contador=1
contador2=0

if n%2==0:
    while contador<=n:
        contador2=contador2+2
        contador=contador+2
        print(contador2)
else:
    while contador<=n-1:
        contador2=contador2+2
        contador=contador+2
        print(contador2)