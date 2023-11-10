valor=float(input("Digite o valor gasto: "))
print("1) Á vista.")
print("2) Dividir em duas vezes.")
print("3) Dividir de 3 até 10 vezes")
forma_pagamento=int(input("Selecione a forma de pagamento: "))

if forma_pagamento==1:
  print(f"Valor a pagar: R${valor-(valor*0.1):.2f}")
elif forma_pagamento==2:
  print(f"Valor a pagar: R${valor:.2f}, pagos em duas vezes de R${valor/2:.2f}")
elif forma_pagamento==3 and valor >100:
  parcelas=int(input("Informe o número de parcelas: "))
  valor_com_juros=(valor/parcelas)+(valor/parcelas*0.3)
  print(f"Valor a pagar: R${valor:.2f}.")
  print(f"Pagos em {parcelas} vezes de R${valor_com_juros:.2f}")