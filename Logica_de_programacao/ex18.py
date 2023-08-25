litro_gas = 2.5
litro_alc = 1.9
comb = input("Informe o combustível (G/A): ")
quant = int(input("Informe a quantidade em litros: "))

if comb == "G" and quant <= 20:
  desconto_gas=litro_gas-(litro_gas*0.025)
  print(f"Valor a pagar: R${desconto_gas*quant:.2f}")
elif comb == "G" and quant > 20:
  desconto_gas=litro_gas-(litro_gas*0.065)
  print(f"Valor a pagar: R${desconto_gas*quant:.2f}")

elif comb == "A" and quant <= 20:
  desconto_alc=litro_alc-(litro_alc*0.035)
  print(f"Valor a pagar: R${desconto_alc*quant:.2f}")
elif comb == "A" and quant > 20:
  desconto_alc=litro_alc-(litro_alc*0.05)
  print(f"Valor a pagar: R${desconto_alc*quant:.2f}")