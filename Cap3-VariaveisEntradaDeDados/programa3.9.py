#Escreva um programa que leia a quantidade de dias, horas, minutos
#e segundos do usuário. Caucule o total em segundos

dias = int(input("Digite o total de dias: "))
horas = int(input("Digite o total de horas: "))
minutos = int(input("Digite o total de minutos: "))
segundos = int(input("Digite o total de horas: "))

dias_conv = dias * 86400
horas_conv=  horas * 3600
minutos_conv= minutos * 60 

total = dias_conv + horas_conv + minutos_conv + segundos
print(f"{dias}dias + {horas}horas + {minutos}minutos + {segundos}segundos, convertido em segundos é de {total}")
