#Escreva um programa que leia dois numeros. Imprima o resultado da multiplicação do primeiro
#pelo segundo. Utilize apenas os operadores de soma e subtração para calcular o resultado.
#Lembre-se de que podemos entender a multiplicação de dois numeros como somas sucessivas de um deles.
#Assim, 4 x 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

resultado = 0
while numero2 > 0:
    resultado = resultado + numero1
    numero2 = numero2 - 1

print(f"O resultado da multiplicação é: {resultado}")