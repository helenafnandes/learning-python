# #############################################################################

# pip install ->  python -m pip install
# ou adicionar o pip às var de ambiente

# ESCOPO DE VARIÁVEIS #########################################################

# Variável global
global_var = 10
print(global_var)  # Saída: 10


def funcao_exemplo():
    # Variável local
    local_var = 5
    print(local_var)   # Saída: 5
    # A variável global_var é sombreada pela variável local_var dentro da função
    global_var = 5
    print(global_var)  # Saída: 5


funcao_exemplo()
print(global_var)  # Saída: 10


def funcao_exemplo2():
    # Modificar uma variável global dentro de uma função,
    global global_var
    global_var = 7
    print(global_var)  # Saída: 7


funcao_exemplo2()

print(global_var)  # Saída: 7

# Tentando acessar a variável local fora da função (gera erro)
# print(local_var)  # NameError: name 'local_var' is not defined


# ENTRADA E SAÍDA #############################################################

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


# IGUALDADE ###################################################################

x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x == y)  # Saída: True
print(x is y)  # Saída: False
print(z is x)  # Saída: True
print(z == x)  # Saída: True


# CONDICIONAIS ################################################################

# Exemplo de operador ternário
idade = 20
maior_de_idade = True if idade >= 18 else False

print(maior_de_idade)  # Saída: True


idade = int(input("Digite sua idade: "))

if idade < 0:
    print("Idade inválida.")
elif idade < 18:
    print("Você é menor de idade.")
else:
    print("Você é maior de idade.")

if True or not True:           # and, or, not
    print("operadores")


# LOOPS #######################################################################

# Exemplo de loop "for" com enumerate()
frutas = ["maçã", "banana", "laranja"]

for indice, fruta in enumerate(frutas):
    print(f"Índice {indice}: {fruta}")

# Saída:
# Índice 0: maçã
# Índice 1: banana
# Índice 2: laranja


nomes = ["Alice", "Bob", "Carlos"]      # 4 elementos
idades = [25, 30, 22, 27]               # 3 elementos

for nome, idade in zip(nomes, idades):
    print(f"{nome} tem {idade} anos.")
# Saída:
# Alice tem 25 anos.
# Bob tem 30 anos.
# Carlos tem 22 anos.


# Exemplo de loop "while" com "else"
contador = 0

while contador < 5:
    print("Contagem:", contador)
    contador += 1
else:
    # quando o while não é interrompido por 'break'
    print("Loop concluído normalmente.")

# Saída:
# Contagem: 0
# Contagem: 1
# Contagem: 2
# Contagem: 3
# Contagem: 4
# Loop concluído normalmente.


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


# LISTAS ######################################################################

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


# CLASSES #####################################################################

class Pessoa:
    # Atributo da classe
    olhos = 2

    def saudacao(self):
        return "Olá, eu sou uma pessoa."

    def metodo(self):
        return "herdar metodo"


class Pessoa2(Pessoa):

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."


pessoa1 = Pessoa()
print(pessoa1.saudacao())   # Saída: Olá!
print(pessoa1.metodo())     # Saída: herdar metodo
print(pessoa1.olhos)        # Saída: 2

pessoa2 = Pessoa2("Alice", 30)
print(pessoa2.saudacao())   # Saída: Olá, meu nome é Alice e eu tenho 30 anos.
print(pessoa2.metodo())     # Saída: herdar metodo
print(pessoa2.olhos)        # Saída: 2
