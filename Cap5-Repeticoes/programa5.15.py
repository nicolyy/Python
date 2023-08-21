#Escreva um programa para controlar uma pequena máquina registradora.
# Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada.
# Utilize a tabela de códigos abaixo para obter o preço de cada produto:
#Seu programa deve exibir o total das compras depois que o usuário digitar 0 (zero).
#Qualquer outro codigo deve gerar a mensagem de erro "Codigo invalido".

#codidos dos produtos e preço
print("COD = 1 | Preço = 0.50.............")
print("COD = 2 | Preço = 1.00.............")
print("COD = 4 | Preço = 4.00.............")
print("COD = 5 | Preço = 7.00.............")
print("COD = 9 | Preço = 8.00.............")

# Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada.
while True:
    codigo = int(input("Digite o codigo do produto(0 para finalizar): "))
    quantidade = int(input("Digite a quantidade: "))
    print("..............................................................")
    
    if codigo == 0:
        break
    if codigo == 1:
        total = quantidade * 0.50
        print(f"{total}")
    if codigo == 2:
        total = quantidade * 1.0
        print(f"{total}")
    if codigo == 3:
        total = quantidade * 4.00
        print(f"{total}")
    if codigo == 5:
        total = quantidade * 7.00
        print(f"{total}")
    if codigo == 9:
        total = quantidade * 8.00
        print(f"{total}")
    else:
        print("Código invalido")
        
    