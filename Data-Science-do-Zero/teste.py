lista = [1, 2, 7, 3, 4, 5]

# sorted tem mais parametros, pesquisar.
lista = sorted(lista)  # orderna a lista

"""
# enumerate é uma tupla com dois valores onde o
# primeiro valor é a posição do objeto e o segundo
# valor é a posição i do objeto
# exemplo abaixo
"""

for i, j in enumerate(lista):
    print(f"Valor de i: {i}")  # posição na lista
    print(f"Valor de j: {j}")  # valor referente a posição na lista


"""
# exemplo com geradores
# geradores são uma forma de criar loops mais eficientes
"""
