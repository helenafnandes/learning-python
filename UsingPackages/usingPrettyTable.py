from prettytable import PrettyTable

table = PrettyTable()


table.add_column("português", ["vermelho", "azul", "amarelo"])
table.add_column("inglês", ["red", "blue", "yellow"])
print(table)

