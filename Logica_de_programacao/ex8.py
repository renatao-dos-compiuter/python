n1=float(input("Digite o primeiro número: "))
n2=float(input("Digite o segundo número: "))
n3=float(input("Digite o terceiro número: "))

if n1<=n2 and n1<=n3:
    print(f"MENOR = {n1}")

elif n2<=n1 and n2<=n3:
    print(f"MENOR = {n2}")

elif n3<=n1 and n3<=n2:
    print(f"MENOR = {n3}")