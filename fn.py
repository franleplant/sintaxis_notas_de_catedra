

def pure(x):
    return x**2

print "FUNCCION PURA"
print pure(2)
print pure(2)
print pure(2)

c = 2

def impure(x):
    return x**c

print "FUNCCION IMPURA"
print impure(2)
c = 3
print impure(2)
c = 4
print impure(2)



cv = [2]
def impure2(x):
    res = x**cv.pop()
    cv.append(res)
    return res

print "FUNCCION IMPURA (automodificante)"
print impure2(2)
print impure2(2)
print impure2(2)


def get(l, i, default):
    try:
        return l[i]
    except IndexError:
        return default

cache = [0 for _ in range(0, 100000)]
def cached_square(x):
    if not get(cache, x, False):
        print "calculando"
        cache[x] = x**2

    return cache[x]


print "CUADRADO CON CACHE (memoization)"
print cached_square(2)
print cached_square(2)
print cached_square(2)


