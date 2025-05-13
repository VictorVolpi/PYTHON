 # 1. Apresente o total de itens da lista exibida abaixo com os meses do
#          ano. Retorno de um número inteiro.

listaMeses2 = ['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
print(len(listaMeses2))

#2. Junte as duas listas em uma terceira lista vazia. Concatene as duas listas.

primeiroSemestre = ['Jan1', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun']
segundoSemestre = ['Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
ano = primeiroSemestre + segundoSemestre
print(ano)

#3 . imprima de maneira separada o primeiro e último iten da lista

ListaValores  = [2200, 3400, 5750, 800, 2000, 1350]
primeiro_item = ListaValores[0]
ultimo_item = ListaValores[-1]

print(f"O primeiro item da lista é {primeiro_item} e o ultimo item é {ultimo_item}.")

# 4 . Adicione o nome Paula Fernandes na posição 2

Nomes = ['Suzy', 'janaina', 'Claudevan', 'Maria Clara']
Nomes.insert(1, 'Paula Fernandes')
print(Nomes)

# 5 Alter o nome Sony para Sony Vaio. Remova o nome Compaq da lista.

Nomes2 = ['Dell', 'Apple', 'Sony', 'Acer', 'Compaq', 'Positivo', 'Lenovo']

    # Alter o nome Sony para Sony Vaio

Nomes2[2] = 'Sony Vaio'

# Remova o nome Compaq da lista.

Nomes2.remove('Compaq')

print(Nomes2)

# 6 .Imprima em ordem numérica crescente (do menor para o maior) a
# lista exibida

desordem =[ 230, 430, 100, 2 , 670, 1212, 321, 89, 6, 34, 20, 9, 99, 710 ]
desordem.sort(reverse=False)
print(desordem)

#7. Imprima em ordem numérica decrescente (do maior para o menor) a lista exibida abaixo

desordem3 =[ 230, 430, 100, 2, 670, 1212, 321, 89, 6, 34, 20, 9, 99, 710 ]
desordem3.sort(reverse=True)
print(desordem3)

# 8. Escreva um programa que leia uma lista(10 valores) de números
# inteiros e imprima a soma de todos os números pares da lista. A
# entrada dos valores deve ser informada pelo usuário.

numeros = []

for _ in range(10):
    valor = int(input("Digite um numero inteiro:"))
    numeros.append(valor)

    #Calcular a soma dos numeros pares

soma_pares = sum(num for num in numeros if num % 2 == 0)

# entrada dos valores deve ser informada pelo usuário.

print(f"A soma dos numeros pares é {soma_pares}")

# 9 . Escreva um programa que leia uma lista(10 valores) de números
# inteiros e imprima a média dos números da lista. Mais uma vez os
# valores devem ser digitados pelo usuário.

lista9 =[]
for i in range (10):
    lista = int (input("digite um numero inteiro"))
    lista9.append (lista)

soma = sum(lista9)
media = soma / len(lista9)
print("a media dos numero é",media)









