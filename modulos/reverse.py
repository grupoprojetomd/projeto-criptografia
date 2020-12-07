from .findXandYCoefficients import computeCoefficients

def reverse(a, m):
    result = computeCoefficients(a, m)

    if (a > m):
        reverse = result['coefficients']['maxNumber']
    else:
        reverse = result['coefficients']['minNumber']
    
    return reverse