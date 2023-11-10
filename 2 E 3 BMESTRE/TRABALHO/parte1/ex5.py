n=int(input("Infrome um valor: "))

if n%2==0:
    while n>=0:
        print(n)
        n-=2
else:
    n-=1
    while n>=0:
        print(n)
        n-=2