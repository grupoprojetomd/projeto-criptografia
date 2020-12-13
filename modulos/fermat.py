def fermat(base, expoente, valorModulo):
    expoenteSimplificado = expoente % (valorModulo - 1)
    resultado = (base ** expoenteSimplificado) % valorModulo

    return resultado

# base = int(input("Base: "))
# expoente = int(input("Expoente: "))
# valorModulo = int(input("Valor módulo: "))

# print(fermat(base, expoente, valorModulo))