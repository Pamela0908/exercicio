'''Exercício 1: Calculadora de Média
Desenvolva um programa em Python que calcula a média de um conjunto
de números inseridos pelo usuário. O programa deve:
Solicitar ao usuário que informe quantos números deseja inserir.
Em um loop, pedir ao usuário que insira cada número.
Armazenar esses números em uma lista.
Calcular a média dos números e exibir o resultado.'''

numeros = []

repeticao = int(input("quantos numeros deseja inserir? :"))

for i in range(repeticao):

    numeros.append (int(input("digite os numeros : ")))

media = (sum(numeros))/repeticao

print (media)