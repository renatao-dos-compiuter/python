base1= float(input("Digite a medida da base do retângulo 1 em cm: "))
altura1= float(input("Digite a medida da altura do retângulo 1 em cm: "))

base2= float(input("Digite a medida da base do retângulo 2 em cm: "))
altura2= float(input("Digite a medida da altura do retângulo 2 em cm: "))

area1= base1*altura1
area2= base2*altura2

if area1== area2:
    print("Os retângulos possuem a mesma área")
else:
    print("Os retângulos não possuem a mesma área")