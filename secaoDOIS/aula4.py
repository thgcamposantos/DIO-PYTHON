# 1.1 Crie dois conjuntos:
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
# Imprima a união, interseção e diferença de A e B.
uniao = A.union(B)
print(f'A união dos dois conjuntos é: {uniao}')

intersecao = A.intersection(B)
print(f'A união dos dois conjuntos é: {intersecao}')

diferença = A.difference(B)
print(f'A união dos dois conjuntos é: {diferença}')


# 1.2 Adicione o número 9 ao conjunto A e remova o número 2. Imprima o conjunto resultante.
adicionar_9 = A.add(9)
print(A)
remover_2 = A.discard(2)
print(A)
# 1.3 Verifique se o número 3 está no conjunto A.
if 3 in A:
    print("Contem")
else:
    print("Não contem")

# 1.4 Crie um conjunto vazio e adicione os elementos 10, 20, 30. Verifique o comprimento do conjunto.
vazio = set()  # Corrigido: cria um conjunto vazio
countF = 3  # Número de vezes que você quer executar o loop

for count in range(countF):  # Corrigido: usa range() para iterar
    numero = int(input("Digite o número: "))  # Pede um número ao usuário
    print(numero)
    vazio.add(numero)  # Adiciona o número ao conjunto (método 'add' é para conjuntos)

print(len(vazio))  # Exibe o conjunto final
