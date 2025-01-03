import math
import modulos

def encriptar(mensagem, chavePublica):

    mensagemTransformada = mensagem.upper()

    letras = {
        'A': 2,
        'B': 3,
        'C': 4,
        'D': 5,
        'E': 6,
        'F': 7,
        'G': 8,
        'H': 9,
        'I': 10,
        'J': 11,
        'K': 12,
        'L': 13,
        'M': 14,
        'N': 15,
        'O': 16,
        'P': 17,
        'Q': 18,
        'R': 19,
        'S': 20,
        'T': 21,
        'U': 22,
        'V': 23,
        'W': 24,
        'X': 25,
        'Y': 26,
        'Z': 27,
        ' ': 28,
    }

    sequenciaDeInteiros = []
    for caractere in mensagemTransformada:
        sequenciaDeInteiros.append(letras[caractere]) 


    equivalentesCifrados = []
    for inteiro in sequenciaDeInteiros:
        equivalenteCifrado = modulos.encontrarEquivalenteCifrado(inteiro, chavePublica[1], chavePublica[0])
        equivalentesCifrados.append(equivalenteCifrado)

    return equivalentesCifrados