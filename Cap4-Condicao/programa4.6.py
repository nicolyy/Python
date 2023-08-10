#Escreva um programa que pergunte a distância que um passageirodeseja percorrer em km. 
#Caucule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200km e 
#R$ 0,45 para viagens mais longas

distancia = int(input("Qual a distancia em KM?: "))
if distancia <= 200:
    cobrar = 0.50
elif distancia >= 200:
    cobrar = 0.45
print(f"O valor total da sua vaigem é {distancia * cobrar}")