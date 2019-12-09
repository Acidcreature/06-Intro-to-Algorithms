# This function raises a number to a given power less efficiently than the pow function native to Python.

def expo(num, power):
    finalnum = num
    count = 1
    while count < power:
        if finalnum == 0:
            finalnum *=  num
            count += 1
        else:
            finalnum *= num
            count += 1
    print(finalnum)
expo(7, 10)