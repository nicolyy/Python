#Altere o programa anterior para exibir os resultados
# no mesmo formato de uma tabuada: 2x1 = 2, 2x2=4, ...

n = int(input("Digite qual tabuada você quer(1, 2, 3..): "))
x = 1

while x <= 10:
    print(f"[{n} x {x} = {n*x}]")
    x = x + 1