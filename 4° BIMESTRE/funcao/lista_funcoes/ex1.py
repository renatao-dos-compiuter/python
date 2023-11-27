def total (x):
    total=x+(salario*(bonus/100)-desconto)
    return total

salario= int(input("Salário: "))
bonus=int(input("Bônus (%): "))
desconto=int(input("Desconto: "))

print(f"Salário lpiquido: {total(salario)}")