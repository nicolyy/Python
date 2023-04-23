#Escreva um programa que pergunte a quantidade de KM percorrido
#por um carro alugado pelo usuário, assim a quantidade de dias pelos quais
#o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa
#R$60 por dia e R$0,15 por km rodado

km = input("Qual a quantidade em KM percorrida?" )
dias = int(input("Qual a quantidade de dias? "))
valor_pagar = (dias * 60) + (km * 0.15)
print(f"O valor total a pagar é de {valor_pagar:5.2f}")