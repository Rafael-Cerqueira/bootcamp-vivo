itens = []

i = 0
while i < 3:
  
  item = input()
  itens.append(item)
  i += 1

print("Lista de Equipamentos:")  
for item in itens:
    print(f"- {item}")