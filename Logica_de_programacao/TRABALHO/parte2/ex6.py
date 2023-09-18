n=int(input("Informe um valor: "))

if n%2==0:
    n-=1
    while n>=0:
        print(n)
        n-=2
else:
     while n>=0:
        print(n)
        n-=2