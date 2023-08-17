#Modifique o programa anterior para imprimir de 1 até o numero digitado 
#pelo usuario, mas dessa vez, apenas os numeros impares

fim = int(input("Digite o ultimo numero a imprimir: "))
x = 1

while x <= fim:
    if x % 3 == 0:
        print(x)
    x = x + 1
print("Muito hacker")