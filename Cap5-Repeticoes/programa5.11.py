#Escreva um programa que pergunte o deposito inicial e a taxa de juros de uma poupanca. 
#Exiba os valores mes a mes para os 24 primeiros meses.
# Escreva o total ganho com juros no periodo.

# Solicita o valor do depósito inicial e a taxa de juros
deposito_inicial = float(input("Digite o valor do depósito inicial: "))
taxa_juros = float(input("Digite a taxa de juros (%): "))

# Converte a taxa de juros para um valor decimal
taxa_decimal = taxa_juros / 100

# Inicializa o contador de meses e o total ganho com juros
mes = 1
total_ganho = 0.0

# Loop para calcular e exibir os valores mês a mês
while mes <= 12:
    juros = deposito_inicial * taxa_decimal
    deposito_inicial += juros
    total_ganho += juros
    print(f"Mês {mes}: Total = R${deposito_inicial:.2f} | Juros = R${juros:.2f}")
    mes += 1

# Exibe o total ganho com juros no período
print(f"Total ganho com juros em 24 meses: R${total_ganho:.2f}")