# inicio = 1
# for inicio in range(inicio , 11 , 1):
#     print(inicio)


# desejo = 's'
# while (desejo == 's'):
#     numero = int(input("Número para contar: "))
#     numero2 = int(input("Número para contar: "))
#     soma = numero + numero2
#     print('A soma é: ' , soma)
#     desejo = str(input('Deseja continuar: '))
# print("A soma final é: " , soma)

# Exercício 3: Tabuada de um Número
# Escreva um programa que solicite ao usuário um número inteiro N e exiba a tabuada de N (de 1 a 10).
tabuada = int(input('Número: '))
for i in range(0 , 10 , 1):
    print(tabuada , " x " , i , " = " , (tabuada * i))