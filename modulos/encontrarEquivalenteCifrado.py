import math
import functools
import operator

def dividirExpoenteEmPotencias(expoente):
    stringBinaria = bin(expoente)

    stringBinaria = stringBinaria[2:]

    stringBinariaInvertida = stringBinaria[::-1]
    
    expoentes = []

    k = 0
    for caractere in stringBinariaInvertida:
        if (caractere == '1'):
            expoentes.append(k)
        
        k += 1


    partesDoExpoente = []
    for expoente in expoentes:
        parteDoExpoente = int(math.pow(2, expoente))
        partesDoExpoente.append(parteDoExpoente)
        
    return partesDoExpoente

def encontrarEquivalenteCifrado(base, expoente, valorModulo):
    partesDoExpoente = dividirExpoenteEmPotencias(expoente) 

    listaDeMods = []
    for expoente in partesDoExpoente:
        if (expoente == 1):
            listaDeMods.append((base ** expoente) % valorModulo)
        else:
            valorSeparado = (base ** int((expoente / 2))) % valorModulo
            listaDeMods.append(((valorSeparado) * (valorSeparado)) % valorModulo)

    a = functools.reduce(operator.mul, listaDeMods)

    resultado = a % valorModulo

    return resultado