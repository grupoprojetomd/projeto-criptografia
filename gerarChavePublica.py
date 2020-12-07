import modulos

def gerarChavePublica(numeroPrimo1, numeroPrimo2, expoente):
    if (not modulos.isPrime(numeroPrimo1) or not modulos.isPrime(numeroPrimo2)):
        return "Erro! É necessário informar números primos"

    expressao = (numeroPrimo1 - 1)*(numeroPrimo2 - 1) # 16

    saoPrimos = (modulos.mdc(expoente, expressao) == 1)

    if (not saoPrimos):
        return "Erro! O expoente informado não é relativamente primo a (p - 1)(q - 1)"

    chavePublica = [
        numeroPrimo1 * numeroPrimo2,
        expoente
    ]

    return chavePublica
