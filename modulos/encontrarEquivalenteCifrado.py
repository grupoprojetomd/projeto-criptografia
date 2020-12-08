import math

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
    print(partesDoExpoente)