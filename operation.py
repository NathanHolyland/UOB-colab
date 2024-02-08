def adding(a, b):
    return a+b

def substract(a, b):
    return a-b

def multiply(*args):
    mult_total = 1
    for argument in args:
        mult_total = mult_total * argument
    return mult_total

def divide(a, b):
    return a/b
