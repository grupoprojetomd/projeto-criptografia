import time
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

def computePrimes(startTime, primes):
    currentNumber = 2
    n = 0

    while((time.time() - startTime) <= 60):
        
        while (currentNumber < 41):
            if (isPrime(currentNumber)):
                primes.append(currentNumber)

            currentNumber += 1

        currentNumber = n*n - n + 41

        if (isPrime(currentNumber)):
            primes.append(currentNumber)
            
        n += 1
        
    return primes