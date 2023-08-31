#escreva uma expressão que sera utilizada para decidir se um
#aluno foi ou não aprovado. Para ser aprovado, todas as médias do aluno
#devem ser maiores que 7, considere que o aluno cursa apenas 3 matérias
#e que a nota de cada uma esta armazenada nas seguintes variavies 
#n1, n2 3 n3

n1 = float(input("Digite a nota em matemática: "))
n2 = float(input("DIgite a nota em PortuguêS: "))
n3=  float(input("Digite a nota em ciências: "))
 
media = (n1 + n2 + n3)/3

if media > 7:
    print(f"Parabéns sua média foi {media:5.1f}, você foi aprovado")
if media < 7:
    print(f"Infelizmente sua média foi {media:5.1f}, você não foi aprovado")