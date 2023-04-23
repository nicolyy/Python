#escreva uma expressão para determinar se uma pessoa deve
#ou não pagar imposto. Considere que pagam impostos de 5% pessoas cujo 
#salário é maior que R$ 1.200,00



#variaveis

nome = input ("Digite o seu nome: ")
salario = float(input("Digite o seu salario, sem pontos ou virgulas:"))
imposto = 5
novo_salario = 0

#metodo e saida
if salario > 1200:
    print("Você pagara imposto")
    
if salario < 1200:
    print("Você não pagara imposto")
    


