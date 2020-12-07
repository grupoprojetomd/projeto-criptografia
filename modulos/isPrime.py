import math

def isPrime(number):
    currentDivisor = 2
        
    maxNumber = int(math.sqrt(number))

    while (currentDivisor <= maxNumber + 1):
        if (number % currentDivisor == 0):
            return 0
        if (currentDivisor == maxNumber + 1):
            return 1

        currentDivisor += 1