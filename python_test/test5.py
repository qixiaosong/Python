list = [1, 2, 3, 4]
it = iter(list)
for x in it:
    print(x, end=" ")


def hello():
    print('hello,python!')
hello()


def printinfo(name, age=20):
    print('name', name)
    print('age', age)
    return
printinfo(name="xiaosong", age=21)
printinfo(name="songsong")
