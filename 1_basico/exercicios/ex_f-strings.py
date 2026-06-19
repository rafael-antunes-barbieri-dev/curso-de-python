nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")

if not nome or not idade:
    print("Desculpe, vc deixou campos vazios")
else:
    idade = int(idade)

if nome and idade:
    print(f"Seu nome é {nome}")
    print("========================================")
    print(f"Seu nome invertido é {nome[::-1]}")
    print("========================================")
    print("Seu nome contém contém espaços?")
    if " " in nome:
        print("Seu nome tem espaços")
    else:
        print("Seu nome não tem espaços")
print("========================================")
print(f"A primeira letra do seu nome é: {nome[0]}")
print("========================================")
