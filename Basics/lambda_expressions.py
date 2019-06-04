from functools import reduce


def f(n): return n ** 3


print(f(2))


def l(n): return "YES" if n % 2 == 0 else "NO"


print(l(6))
print(l(5))
print(l(7))
print(l(16))


def s(a, b): return a + b


print(s(2, 22))

# filter lambda

lst1 = [2, 4, 6, 8, 11, 13, 15]

filtered_list = list(filter(lambda x: x % 2 == 0, lst1))
print(filtered_list)

# map lambda
map_result = list(map(lambda n: n * 2, lst1))
print(map_result)

# reduce lambda
result = reduce(lambda x, y: x + y, lst1)
print(result)
