#Crie uma lista com os nomes de 5 frutas. Em seguida, peça ao usuário para digitar uma fruta e verifique se ela está presente na lista. Imprima uma mensagem informando se a fruta foi encontrada ou não.

# bia = ["Morango" ,"Abacaxi" , "Uva" , "Manga" , "Melancia"]

# frutas = input("Digite o nome da lista: ")
# if frutas in bia:
#     print(bia.index(frutas))
# else:
#     print(False)


#Crie uma lista com 10 números inteiros. Calcule e imprima a soma de todos os elementos da lista.
# numeros = [1 ,2 , 3 ,4 , 5 , 6 , 7 , 8 , 9 , 10]
# soma = 0

# for numero in numeros:
#     soma += numero

# print(f"A soma dos elementos é  {soma}")

#Crie uma lista com os nomes de 5 países. Ordene a lista em ordem alfabética e imprima o resultado
# paises = ["Brasil" , "Argentina" , "Peru" , "Uruguai" , "Colombia"]

# paises_ordenada = paises.copy()
# paises_ordenada.sort()
# print(paises_ordenada)

#Crie uma lista com 10 números inteiros. Remova todos os números pares da lista e imprima a lista resultante.
numeros = [1 ,2 , 3 ,4 , 5 , 6 , 7 , 8 , 9 , 10]
cont = 0
for numero in numeros:
    if numero % 2 == 0:
        numeros.pop(cont)
        cont += 1
    else:
        cont += 1

print(numeros)



 