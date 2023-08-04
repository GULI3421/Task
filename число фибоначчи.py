"""# числа фибоначчи

f1 = f2 = 1
n = 10
print(f1, end=' ')
print(f2, end=' ')
for i in range(2, n):
    f1, f2, = f2, f1 + f2 #сумма двух предыдущих чисел
    print(f2, end=' ')"""

"""import math
def fib(n):
    golden_ration = (1 + math.sqrt(5)) / 2
    val = (golden_ration**n - (1 - golden_ration)**n) / math.sqrt(5)
    return int(round(val))
print(fib(70))"""

def fib():
    f1,f2 = 0, 1
    while True:
        yield f1
        f1, f2 = f2, f1 + f2
for i, f in zip(range(10+1), fib()):
    print("{i:3}: {f:3}".format(i=i, f=f))  
