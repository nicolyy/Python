#Escreva um programa que leia três numeros e que imprima o maior e o menor

n1 = int(input("Digite o primeiro numero inteiro: "))
n2 = int(input("Digite o segundo numero inteiro: "))
n3 = int(input("Digite o terceiro numero inteiro: "))

if n1 >= n2 and n1>= n3:
    maior = n1
elif n2 >= n1 and n2>= n3:
    maior = n2
elif n3 >= n2 and n3>= n1:
    maior = n3

if n1 <= n2 and n1 <= n3:
    menor = n1
elif n2 <= n1 and n2<= n3:
    menor = n2
elif n3 <= n2 and n3<= n1:
    menor = n3
    
print(f"O maior numero é {maior}")
print(f"O menor numero é {menor}")
        
