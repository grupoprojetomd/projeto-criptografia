import modulos

def desencriptar(mensagemCriptografada, expoente, numeroPrimo1, numeroPrimo2):
    if (not modulos.isPrime(numeroPrimo1) or not modulos.isPrime(numeroPrimo2)):
        return {
            'erro': "Erro! É necessário informar números primos",
            'chavePublica': 0
        }

    expressao = (numeroPrimo1 - 1)*(numeroPrimo2 - 1)

    saoPrimos = (modulos.mdc(expoente, expressao) == 1)

    if (not saoPrimos):
        return {
            'erro': "Erro! O expoente informado não é relativamente primo a (p - 1)(q - 1)",
            'chavePublica': 0
        }

    letras = {
        2: 'A',
        3: 'B',
        4: 'C',
        5: 'D',
        6: 'E',
        7: 'F',
        8: 'G',
        9: 'H',
        10: 'I',
        11: 'J',
        12: 'K',
        13: 'L',
        14: 'M',
        15: 'N',
        16: 'O',
        17: 'P',
        18: 'Q',
        19: 'R',
        20: 'S',
        21: 'T',
        22: 'U',
        23: 'V',
        24: 'W',
        25: 'X',
        26: 'Y',
        27: 'Z',
        28: ' '
    }

    d = modulos.reverse(expoente, expressao)

    dCorreto = modulos.putXOnInterval(d, expressao)

    n = numeroPrimo1 * numeroPrimo2
    mensagemDescriptografada = []

    for inteiro in mensagemCriptografada:
        equivalenteCifrado = modulos.encontrarEquivalenteCifrado(int(inteiro), d, n)
        
        mensagemDescriptografada.append(letras[equivalenteCifrado])

    mensagemFinal = ''.join(mensagemDescriptografada)

    return mensagemFinal