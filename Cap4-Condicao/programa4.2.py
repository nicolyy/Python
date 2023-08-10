#Escreva um programa que pergunte a velocidade do carro de um usuário. 
#Caso ultrapasse 80km/h, exiba uma mensagem dizendo que o usuário foi multado
#Nesse caso, exiba o valor da multa, cobrando R$: 5 por km acima de 80 km/h

velocidade = int(input("Qual a velocidade do carro: "))
if velocidade > 80:
    multado = True
    print("Você foi multado")
    if True:
        multa = (velocidade - 80) * 5
        print(f"Sua multa é {multa}")

    