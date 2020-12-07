import operator
import functools
from .findSolutionOfCongruence import putXOnInterval
from .findSolutionOfCongruence import findSolutionOfCongruence

def calcularMMaior(arrayDeMsMenores):
    multiplicacao = functools.reduce(operator.mul, arrayDeMsMenores)
    return multiplicacao

def encontrarSolucaoTeoremaChines(arrayDeBs, arrayDeMsMenores):
    valorDeMMaior = calcularMMaior(arrayDeMsMenores)

    arrayDeMsMaiores = []
    arrayDosRestos = []
    arrayDeSolucoes = []
    x0 = 0

    totalDePosicoes = len(arrayDeMsMenores)

    for posicao in range(totalDePosicoes):
        valorDeMMaiorAtual = int(valorDeMMaior / arrayDeMsMenores[posicao])
        arrayDeMsMaiores.append(valorDeMMaiorAtual)

        restoAtual = int(arrayDeBs[posicao] % arrayDeMsMenores[posicao])
        arrayDosRestos.append(restoAtual)

        solucaoAtual = findSolutionOfCongruence(valorDeMMaiorAtual, 1, arrayDeMsMenores[posicao])
        arrayDeSolucoes.append(solucaoAtual)

        x0 += valorDeMMaiorAtual*restoAtual*solucaoAtual

    correctX0 = putXOnInterval(x0, valorDeMMaior)

    return correctX0