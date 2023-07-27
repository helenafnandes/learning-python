# Exemplo de loop "while"
contador = 0

while contador < 5:
    print("Contagem:", contador)
    contador += 1

# Saída: 0 a 4


# Exemplo de loop "for"
frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:
    print("Gosto de", fruta)

# Saída:
# Gosto de maçã
# Gosto de banana
# Gosto de laranja


# Exemplo de loop "for" usando a função "range()"
for numero in range(1, 6):  # O intervalo vai de 1 a 5 (6 não é incluído)
    print(numero)

# Saída: 1 a 5


idade = int(input("Digite sua idade: "))

if idade < 0:
    print("Idade inválida.")
elif idade < 18:
    print("Você é menor de idade.")
else:
    print("Você é maior de idade.")

if True or not True:           # and, or, not
    print("operadores")


idade = 30
cidade = "São Paulo"
# Imprimindo múltiplos valores com a vírgula , -> espaços automáticos
print("Idade:", idade, "anos. Cidade: " + cidade)
# Saída: Idade: 30 anos. Cidade: São Paulo

print("Tip Calculator")
print("Total bill: R$", end="")
total_bill = int(input())
print("n. of people to split the bill: ")
people = int(input())

each = total_bill / people
print(f"Each person should pay: R${each}")

two_digit_number = input("enter a 2 digit number: ")
first_digit = int(two_digit_number[0])  # int
second_digit = int(two_digit_number[1])    # str
print(f"{first_digit} + {second_digit} = {first_digit+second_digit}")
print(first_digit, "+", second_digit, "=", first_digit+second_digit)


x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x == y)  # Saída: True
print(x is y)  # Saída: False
print(z is x)  # Saída: True
print(z == x)  # Saída: True


# Criando uma lista inicial
frutas = ["maçã", "banana", "laranja", "uva"]

# Imprimindo a lista completa
print("Lista original:", frutas)

# Acessando um elemento da lista pelo índice
print("Primeira fruta:", frutas[0])  # Saída: maçã

# Modificando um elemento da lista
frutas[1] = "abacaxi"
print("Lista após modificar:", frutas)

# Adicionando elementos à lista
frutas.append("morango")
print("Lista após adicionar morango:", frutas)

# Removendo um elemento da lista
frutas.remove("laranja")
print("Lista após remover laranja:", frutas)

# Inserindo um elemento em uma posição específica
frutas.insert(1, "pêra")
print("Lista após inserir pêra na posição 1:", frutas)

# Contando o número de ocorrências de um elemento na lista
ocorrencias_uva = frutas.count("uva")
print("Ocorrências de uva na lista:", ocorrencias_uva)

# Ordenando a lista em ordem alfabética
frutas.sort()
print("Lista ordenada:", frutas)

# Revertendo a ordem dos elementos na lista
frutas.reverse()
print("Lista revertida:", frutas)

# Fatiando (slicing) a lista para obter uma parte dela
parte_da_lista = frutas[1:4]
print("Parte da lista:", parte_da_lista)

# Verificando se um elemento está presente na lista
if "morango" in frutas:
    print("Sim, morango está na lista.")
else:
    print("Não, morango não está na lista.")


# Removendo o elemento no índice 2 (laranja) e retornando o elemento removido
# pop() sem índice remove e retorna o último elemento
elemento_removido = frutas.pop(2)
print("Elemento removido:", elemento_removido)
print("Lista após remover o elemento:", frutas)

# Removendo o elemento no índice 2 (laranja) usando a palavra-chave del
del frutas[2]
print("Lista após remover o elemento:", frutas)
