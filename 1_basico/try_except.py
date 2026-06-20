# try -> tentar executar o codigo
# except -> ocorreu algum erro ao tentar executar

numero_str = input("Digite um numero para ser dobrado: ")

try:
    numero_float = float(numero_str)
    print(f"O dobro de {numero_str} é: {numero_float * 2}")
except:
    print("Digita algo válido, seu burro")

"""
Não é recomendado se usar o try/except desta forma
No entanto, esta foi uma aula básica para aprender o conceito
"""
