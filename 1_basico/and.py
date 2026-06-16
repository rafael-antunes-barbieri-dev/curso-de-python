escolha = input("[E]entrar [S]sair: ")
senha_digitada = input("Senha: ")
senha_permitida = str(123456)

if escolha == "E" and senha_digitada == senha_permitida:
    print("Entrou")
elif escolha == "E":
    print("Senha incorreta")
else:
    print("Saiu")
