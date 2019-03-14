

def fib(n):
    a = 1
    b = 0
    for i in range(n):
        aux_a = a
        a = a + b
        b = aux_a

    return a

for i in range(10):
    print fib(i)

