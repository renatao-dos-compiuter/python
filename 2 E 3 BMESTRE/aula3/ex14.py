escala=input("Você vai digitar a temperatura em qual escala (C/F)? ")
if escala=="F":
  fahreinheit=float(input("Digite a temperatura em Fahrenheit: "))
  celsius=(5/9)*(fahreinheit-32)
  print(f"Temperatura equivalente em Celsius: {celsius:.2f}")
elif escala=="C":
  celsius=float(input("Digite a temperatura em Celsius: "))
  fahreinheit=celsius*1.8+32
  print(f"Temperatura equivalente em Fahreinheit: {fahreinheit:.2f}")
