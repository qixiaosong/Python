'''
def normalize(name):
    return (name.lower()).capitalize()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

from functools import reduce


def prod(L):
    return reduce(lambda a, b: a * b, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

#判断（0~1000）的 回数
def is_palindrome(n):
    return str(n) == str(n)[::-1]

output = filter(is_palindrome, range(1, 1000))
print(list(output))


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0]  # ^.^发现自己好聪明啊2333

print(sorted(L, key=by_name))
print(sorted(L, key=lambda t: t[1]))
print(sorted(L, key=lambda t: t[1])[::-1])	#两种写法，成绩从大到小
print(sorted(L, key=lambda t: t[1], reverse=True))


#闭包

def count():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())
'''