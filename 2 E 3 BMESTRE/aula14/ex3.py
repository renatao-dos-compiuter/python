tabuada=int(input("Montar a tabuada de: "))
start=int(input("Começar por: "))
end=int(input("Terminar em: "))

if end>start:
    for i in range (start, end+1):
        print(f"{tabuada} X {i} = {tabuada*i}")
else:
    print("O número final não pode ser menor que o inicial")