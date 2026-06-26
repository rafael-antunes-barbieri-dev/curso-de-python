"""
while (enquanto)
executa algo enquanto for verdadeiro
"""

while True:  # Loop infinito
    nome = input("Digite o seu nome: ")
    print(f"Seu nome é {nome}")

    if nome == "sair":
        break

print("saiu")


contador = 0

while contador <= 10:
    contador += 1

    if contador == 6:
        continue

    print(contador)
