#Escreva um programa que pergunte o salário do funcionário e caucule o valor 
#do aumento. Para salários superiores a R$ 1250, caucule aumento de 10%. Para os inferiores ou iguais 15%

salario = float(input("Digite o seu salario: "))
if salario > 1250:
    aumento = 10
elif salario <= 1250:
    aumento = 15

valor_aumento = (salario * aumento)/100
print(f"Seu aumento foi de {valor_aumento}")
print(f"O valor total do novo salario é: {salario + valor_aumento}")