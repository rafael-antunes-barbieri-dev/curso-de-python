"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

print("Exercicio 1:")
numero = input("Digite um número inteiro: ")

if numero.isdigit():
    numero = int(numero)
else:
    print("Digite um número valido")

if numero % 2 == 0:
    print("O número digitado é par")
else:
    print("O número digitado é ímpar")

print("====================================")

print("Exercicio 2:")
hora = input("Digite as horas (0-23):")

if hora.isdigit():
    hora = int(hora)

    if hora >= 0 and hora <= 11:
        print("manhã")
    elif hora >= 12 and hora <= 17:
        print("tarde")
    else:
        print("noite")

else:
    print("Digite um valor válido")

print("====================================")

print("Exercicio 3:")
primeiro_nome = input("Digite o seu primeiro nome: ")

if " " in primeiro_nome:
    primeiro_nome = primeiro_nome.replace(" ", "")
    print("Espaços e sobrenomes removidos com sucesso")

if len(primeiro_nome) <= 4:
    print("nome curto")
elif len(primeiro_nome) >= 5 and len(primeiro_nome) <= 6:
    print("nome normal")
else:
    print("nome longo")
