#Modifique o programa anterior para que aceite respostas com 
# letras maiusculas e minusculas em todas as questoes.

pontos = 0
questao = 1

while questao <= 3:
    resposta = input(str(f"Resposta da questao {questao}: "))
    if questao == 1 and resposta == "b" or resposta == "B":
        pontos = pontos + 1
    if questao == 2 and resposta == "a" or resposta == "A":
        pontos = pontos + 1
    if questao == 3 and resposta == "d" or resposta == "D":
        pontos = pontos + 1
    questao = questao + 1 
print(f"O aluno fez {pontos} pontos")