from .reverse import reverse

def putXOnInterval(x, m):
    if (x > m or x < 0):
        return putXOnInterval(x % m, m)
    
    return x

def findSolutionOfCongruence(a, b, m):
    reverseNumber = reverse(a, m)

    x = reverseNumber * b

    correctX = putXOnInterval(x, m)

    return correctX