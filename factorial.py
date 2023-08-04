n = int(input('n = '))
def factorial_recursive(n):
    if n == 1:
        return n
    else:
        return n*factorial_recursive(n-1)
print(factorial_recursive(n))

"""def fac(n):
    if n == 0:
        return 1
    return fac(n-1)*n
print(fac(5))"""
