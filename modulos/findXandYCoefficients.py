def euclidesAlgorithmToReturnQuotients(number1, number2, listOfQuotient):
    rest = number1 % number2

    if (rest == 0):
        return {
            'quotients': listOfQuotient,
            'mdc': number2
        }
    
    quotient = int(number1 / number2) # 2

    currentListOfQuotient = listOfQuotient + [quotient] # [0, 2]

    return euclidesAlgorithmToReturnQuotients(number2, rest, currentListOfQuotient) # 3, 1, [0, 2]

def findXYCoefficients(listOfQuotients, listOfCoefficients, iterator, finalListOfCoefficients):
    isPenultimateCoefficient = (len(listOfQuotients) - 2) == iterator
    isLastCoefficient = (len(listOfQuotients)- 1) == iterator
    
    if (listOfCoefficients == [1]):
        
        nextCoefficient = listOfQuotients[iterator] * 1

        listOfCoefficients.append(nextCoefficient)

        if (isPenultimateCoefficient):
            finalListOfCoefficients.append(nextCoefficient)
        elif (isLastCoefficient):
            finalListOfCoefficients.append(nextCoefficient * (-1))

        return findXYCoefficients(listOfQuotients, listOfCoefficients, iterator + 1, finalListOfCoefficients)
    

    nextCoefficient = (listOfQuotients[iterator] * listOfCoefficients[iterator]) + listOfCoefficients[iterator - 1] # 1
    
    if (isPenultimateCoefficient):
        finalListOfCoefficients.append(nextCoefficient)
    elif (isLastCoefficient):
        finalListOfCoefficients.append(nextCoefficient)

        isCoefficientsQuantityEven = len(listOfQuotients) % 2 == 0

        if (isCoefficientsQuantityEven):
            finalListOfCoefficients[0] *= -1
        else:
            finalListOfCoefficients[1] *= -1

        return finalListOfCoefficients

    listOfCoefficients.append(nextCoefficient)

    return findXYCoefficients(listOfQuotients, listOfCoefficients, iterator + 1, finalListOfCoefficients)


def computeCoefficients(number1, number2):
    if (number1 > number2):
        maxNumber = number1
        minNumber = number2
    else:
        maxNumber = number2
        minNumber = number1 

    euclidesResult = euclidesAlgorithmToReturnQuotients(minNumber, maxNumber, [])

    quotients = euclidesResult['quotients']
    mdc = euclidesResult['mdc']

    quotients.reverse() 

   

    coefficientsXY = findXYCoefficients(quotients, [1], 0, [])

    coefficients = {
        'maxNumber': coefficientsXY[1],
        'minNumber': coefficientsXY[0]
    }

    return {
        'coefficients': coefficients,
        'maxNumber': maxNumber,
        'minNumber': minNumber,
        'mdc': mdc
    }
