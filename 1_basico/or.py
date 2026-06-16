escolha = input("[E]entrar [S]sair: ")
senha_digitada = str(input("Senha: "))
senha_permitida = str(123456)

if (escolha == "E" or "e") and senha_digitada == senha_permitida:
    print("Entrou")
elif escolha == "E" or "e":
    print("Senha incorreta")
else:
    print("Saiu")
