sal = float(input("Digite o salário da pessoa: "))
if sal <= 1000:
  sal_aumentado = sal + (sal * 0.2)
  print(f"Novo salário = R$ {sal_aumentado:.2f}")
  print(f"Aumento = R$ {sal*0.2:.2f}")
  print("Porcentagem = 20%")
elif sal > 1000 and sal <= 3000:
  sal_aumentado = sal + (sal * 0.15)
  print(f"Novo salário = R$ {sal_aumentado:.2f}")
  print(f"Aumento = R$ {sal*0.15:.2f}")
  print("Porcentagem = 15%")
elif sal > 3000 and sal <= 8000:
  sal_aumentado = sal + (sal * 0.1)
  print(f"Novo salário = R$ {sal_aumentado:.2f}")
  print(f"Aumento = R$ {sal*0.1:.2f}")
  print("Porcentagem = 10%")
else:
  sal_aumentado = sal + (sal * 0.05)
  print(f"Novo salário = R$ {sal_aumentado:.2f}")
  print(f"Aumento = R$ {sal*0.05:.2f}")
  print("Porcentagem = 5%")