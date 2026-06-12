# if / elif      / else
# se / se não se / caso contrário

print("1. Entrar no sistema")
print("2. Sair do sistema\n")

escolha_numero = int(input("Selecione um número: "))

if escolha_numero == 1:
    print("Entrou no sistema")
elif escolha_numero == 2:
    print("Saiu do sistema")
else:
    print("Escolha um número válido")