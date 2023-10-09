def add(a, b):

    if not isinstance(a, (int, float)):
        raise TypeError("a must be int or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be int or float")

    return a + b

def sub(a, b):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be int or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be int or float")

    return a - b

def square(b):
    if not isinstance(b, (int, float)):
        raise TypeError("b must be int or float")

    return round(b * b, 2)

f = add(40, 30)
g = square(5.4)
print(f)
print(g)
