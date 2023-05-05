#Escreva um programa que caucule o tempo de uma viagem de carro
#Pergunte a distancia a percorrer e a velocidade média esperada para a viagem

distancia = float(input("Qual será a distancia percorrida? "))
velocidade = int(input("Qual será a velocidade média percorrida? "))

tempo = distancia / velocidade 
print("O tempo da sua viagem sera de {tempo}")