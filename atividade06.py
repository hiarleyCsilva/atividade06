# Digite um numero interio e veja sua tabuada
numero32= int(input("digite um numero:"))
print(f"Tabuada de {numero32}:")
for i in range(1, 11):
    resultado = numero32 * i
    print(f"{numero32} x {i} = {resultado}")