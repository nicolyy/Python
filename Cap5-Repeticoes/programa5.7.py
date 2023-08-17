#Modifique o programa anterior de forma que o
# usuario tambem digite o inicio e o fim da tabuada, em vez de comecar com 1 e 10.

x = 1

n = int(input("Digite qual tabuada você quer(1, 2, 3..): "))
print("....................................................................")
inicio = int(input("Digite o numero que gostaria de iniciar a tabuda: "))
print("....................................................................")
fim = int(input("Digite o ultimo numero a ser multiplicado: "))
print("....................................................................")
print("TABUADA")
print("....................................................................")

while inicio <= fim:
    print(f"{inicio} x {n} = {inicio*n}]")
    inicio = inicio + 1
    print("....................................................................")


#estava querendo colocar uma decoração