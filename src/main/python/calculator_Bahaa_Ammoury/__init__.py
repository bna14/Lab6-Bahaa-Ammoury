def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x/y
def modulus(x, y):
    return x % y

def exponentiation(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    return x ** 0.5