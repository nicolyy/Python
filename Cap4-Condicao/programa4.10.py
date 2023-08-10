#Escreva um programa que caucule o preço a pagar pelo fornecimento de energia elétrica. 
#Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para industrias
# e C para comércios. Caucule o preço a pagar de acordo com a tabela a seguir (no livro)

kwh = int(input("Qual a quantidade de KWH consumida? : "))
print("Qual o tipo de residencia?")
print("R = Residencia")
print("I = Industrias")
print("C = Comercio")

instalacao = str(input("Digite a opção: "))

if instalacao == "R" and kwh <= 500:
    valor = 0.40
elif kwh > 500:
    valor = 0.65
if instalacao == "I" and kwh <= 1000:
    valor = 0.55
elif kwh > 1000:
    valor = 0.60
if instalacao == "C" and kwh <= 5000:
    valor = 0.55
elif kwh > 5000:
    valor = 0.60

print(f"O valor da sua conta é: {kwh * valor}")