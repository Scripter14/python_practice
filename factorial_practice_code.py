'''def factorial(n):
    return n * factorial(n - 1)


print(factorial(4))'''
def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)


print(fun(25))
