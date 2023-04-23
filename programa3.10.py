#Faça um programa que caucule o aumento de um salário. 
#Ele deve solicitar o valor do salário e a porcentagem do aumento
#Exiba o valor do aumento e do novo salário

salario = int(input("Digite o valor do seu salario: "))
aumento = int(input("Digite a porcentagem de aumento: "))

novo_salario = salario + ((salario * aumento)/100)
print("Seu novo salário é: {novo_salario}")