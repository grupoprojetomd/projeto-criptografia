import modulos

def gerarChavePublica(numeroPrimo1, numeroPrimo2, expoente):
    if (not modulos.isPrime(numeroPrimo1) or not modulos.isPrime(numeroPrimo2)):
        return 0

    expressao = (numeroPrimo1 - 1)*(numeroPrimo2 - 1)

    saoPrimos = (modulos.mdc(expoente, expressao) == 1)

    if (not saoPrimos):
        return 0

    return 1
    


    