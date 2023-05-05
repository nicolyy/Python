#Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto
#exiba o valor do desconto e o preço a pagar

preco = float(input ("Digite o valor da mercadoria: "))
porcentual = int(input("DIgite o valor o porcentual de desconto: "))

desconto = (preco * porcentual)/100
total = preco - desconto
print(f"O desconto foi de: {desconto}, o valor final é: {total:5.2f}")
