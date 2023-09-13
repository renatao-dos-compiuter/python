a= float(input("coeficiente a:  "))
b= float(input("coeficiente b:  "))
c= float(input("coeficiente c:  "))

delta= (b*b)-(4*a*c)
if delta<0:
    print("Essas equação não possuí raízes reais")

else:
    bhaskara1= (-b+(delta**1/2)/2*a)
    bhaskara2= (-b-(delta**1/2)/2*a)
    print(f"x1= {bhaskara1:.4f}")
    print(f"x2= {bhaskara2:.4f}")