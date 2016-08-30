a = "hello python"
print(a[0])
print("修改过的a:", (a[:6] + "world!") * 2)
if("h" in a):
    print("ture")
else:
    print("flase")
print("I am %s ,%d years old." % ('qixiaosong', 21))
str = "this is my frist python example!"
print("str.capitalize()", str.capitalize())
print("str.center(40, '*')", str[:4].center(40, '*'))
print("str.count()", str.count('i', 0, 20))
# python列表：
list = ['qixiaosong', 'song', 1995, 2016]
list[2] = 'songsong'
print(list)
del list[0]
print("list的长度：", len(list))
list = ['qi', 'xiao', 'song']
list.sort()
print(list)
# python元组：
# 与列表的不同，元组元素不能改变，小括号
tul1 = ()
tul1 = (10,)
# 字典：
dict = {"d1": 123, 'd2': 456}
print(dict["d1"])
a, b = 0, 1
while b < 10:
    print(b, end=',')
    a, b = b, a + b
input('点击 enter 键退出')
