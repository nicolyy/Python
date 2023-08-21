#Escreva um programa que leia números inteiros do teclado. 
# O programa deve ler os números até que o usuário digite 0 (zero).
# No final da execução, exiba a quantidade de números digitados, 
# assim como a soma e a média aritmética.

# Inicialização das variáveis
soma = 0
contador = 0

# Leitura dos números e cálculos
while True:
    numero = int(input("Digite um número inteiro (0 para sair): "))
    
    if numero == 0:
        break  # Sai do loop quando o número digitado for 0
    
    soma += numero
    contador += 1

# Verifica se algum número foi digitado antes de calcular a média
if contador == 0:
    print("Nenhum número foi digitado.")
else:
    media = soma / contador
    print(f"Quantidade de números digitados: {contador}")
    print(f"Soma dos números: {soma}")
    print(f"Média dos números: {media:.2f}")