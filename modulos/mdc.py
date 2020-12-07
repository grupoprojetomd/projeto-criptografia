def mdc(number1, number2):
    rest = number1 % number2
    
    if (rest == 0):
        return number2
    
    return mdc(number2, rest)