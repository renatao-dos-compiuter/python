n1 = float(input("Digite a sua primeira nota: "))
n2 = float(input("Digite a sua segunda nota: "))

nota_fi= n1+n2

if nota_fi >=60:
    print(f"NOTA FINAL = {nota_fi:.1f}")
else:
    print(f"NOTA FINAL =  {nota_fi:.1f} REPROVADO!")