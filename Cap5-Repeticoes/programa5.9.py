dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))

quociente = 0
while dividendo >= divisor:
    dividendo -= divisor
    quociente += 1

resto = dividendo

print(f"Quociente: {quociente}")
print(f"Resto: {resto}")