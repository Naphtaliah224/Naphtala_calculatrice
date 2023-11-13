def calculate_exponential(base, exponent):
    return base ** exponent


def calculate_factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Factorial is only defined for positive integers")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def calculate_square_root(num):
    if num < 0:
        raise ValueError("You can't calculate the square root of a negative number")
    return num ** 0.5


def modulo(a, b):
    
    if b == 0:
        raise ValueError("Le diviseur ne peut pas être zéro.")
    return a % b

def racine_nieme(x, n):

    if n <= 0:
        raise ValueError("L'indice de la racine doit être supérieur à zéro.")
    return x ** (1/n)




def carree(x):
    return x ** 2


def valeur_absolue(x):

    return x if x >= 0 else -x
