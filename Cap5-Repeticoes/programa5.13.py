#Escreva um programa  que pergunte o valor inicial de uma divida e o juros mensal.
# Pergunte também o valor mensal que será pago.
# Imprima o número de meses para que a divida seja paga, 
# o total pago e o total de juros pago.

# Entrada dos valores iniciais
divida_inicial = float(input("Digite o valor inicial da dívida: "))
juros_mensal = int(input("Digite o juros mensal em porcentagem: ")) / 100
pagamento_mensal = float(input("Digite o valor mensal a ser pago: "))

# Inicialização das variáveis
meses = 0
total_pago = 0
total_juros = 0

# Cálculos e iteração usando while
while divida_inicial > 0:
    juros_pago = divida_inicial * juros_mensal
    total_juros += juros_pago
    
    if pagamento_mensal >= divida_inicial + juros_pago:
        pagamento_mensal = divida_inicial + juros_pago
    
    divida_inicial = divida_inicial + juros_pago - pagamento_mensal
    total_pago += pagamento_mensal
    meses += 1
    
    print(f"Total de meses para pagar a dívida: {meses}")
    print(f"Total pago: R${total_pago:.2f}")
    print(f"Total de juros pagos: R${total_juros:.2f}")
    if divida_inicial == 0:
        print("ACabou")

# Saída dos resultados
