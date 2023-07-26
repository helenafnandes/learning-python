print("Hello World")

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


# (is vs. ==) is checks if two variables refer to the same object, but == checks
# if the objects pointed to have the same values.
a = [1, 2, 3, 4]  # Point a at a new list, [1, 2, 3, 4]
b = a             # Point b at what a is pointing to
b is a            # => True, a and b refer to the same object
b == a            # => True, a's and b's objects are equal
b = [1, 2, 3, 4]  # Point b at a new list, [1, 2, 3, 4]
b is a            # => False, a and b do not refer to the same object
b == a            # => True, a's and b's objects are equal

li = []
li.append(1)
li.append(2)
li.append(4)
# Access a list like you would any array
li[0]   # => 1
# Look at the last element
li[-1]  # => 3
# You can look at ranges with slice syntax.
# The start index is included, the end index is not
# (It's a closed/open range for you mathy types.)
li[1:3]   # Return list from index 1 to 3 => [2, 4]
li[2:]    # Return list starting from index 2 => [4, 3]
li[:3]    # Return list from beginning until index 3  => [1, 2, 4]
li[::2]   # Return list selecting every second entry => [1, 4]
li[::-1]  # Return list in reverse order => [3, 4, 2, 1]
