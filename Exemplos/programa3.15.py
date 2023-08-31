#Escreva um programa para caucular a redução do tempo de vida
#de um fumante. Pergunte a quantidade de cigarros fumado por dia e quantos anos
#ele já fumou. Considere que um fumante perde 10min de vida a cada cigarro 
#Caucule quantos dias de vida um fumante perderá. Exiba o total em dias

cigarro = int(input("Qual a quantidade de cigarro você fuma por dia? "))
anos = int(input("Quantos anos você fuma?"))
total_cigarro = (anos * 365) * cigarro
perda_min = total_cigarro * 10
perda_dia= (perda_min / 60)/24

print("Você perdera o total de {perda_dia}")