# EXEMPLO

# idade = int(input('Qual sua idade: '))
# if(idade < 12):
#     print('Criança')
# elif(idade >= 12 and idade < 18):
#     print('Adolescente')
# else:
#     print('Adulto')

# # Exercício 1: Verificação de Número Par ou Ímpar
# Escreva um programa que solicite ao usuário um número inteiro e determine se ele é par ou ímpar.
#   numero = int(input('Informe um número: '))
#       if(numero % 2 == 0):
#           print('Número par')
#       else:
#           print('Número impar')

# Exercício 3: Classificação de Notas
#Escreva um programa que solicite ao usuário uma nota (entre 0 e 100) e classifique essa nota em: "F" (0-59), "D" (60-69), "C" (70-79), "B" (80-89), "A" (90-100).
nota = int(input('Informe sua nota: '))
if(nota <= 59):
    print('Nota F')
elif (nota > 59 and nota < 69):
    print('Nota D')
elif (nota > 69 and nota < 79):
    print('Nota C')
elif (nota > 79 and nota < 89):
    print('Nota B')
else:
    print('Nota A')