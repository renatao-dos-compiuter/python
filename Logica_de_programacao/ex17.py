print("Digite dois números inteiros positivos:")
num1 = int(input())
num2 = int(input())
if num1>num2 and num1 % num2 == 0 or num2>num1 and num2 % num1 == 0:
  print("São múltiplos")
elif num1 == 0 or num2 == 0:
  print("Só é múltiplo de zero, o próprio zero")
else:
  print("Não são múltiplos")