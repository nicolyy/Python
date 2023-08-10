#escreva um programa que leia dois numeros e que pergunte qual operação você deseja realizar
#Você deve poder caucular soma, subtração, multiplicação ou divisão. Exiba o resultado 
#da operação solicitada

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
print("Selecione o operador que deseja")
print(" Soma = 1\n Subtração = 2\n Multiplicação = 3\n Divisão = 4")
operador = int(input("Qual o operador?: "))
if operador == 1:
    operacao = n1 + n2
elif operador == 2:
    operacao = n1 - n2
elif operador == 3:
    operacao = n1 * n2
elif operador == 4:
    operacao = n1 / n2
print(f"Resultado = {operacao}")
