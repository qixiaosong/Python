import random
print(random.random())
print(random.sample(range(10), 2))
print(random.choice(['apple', 'xiaomi', 'huawei']))
print(random.randint(1, 10))
print(random.randrange(10))

from datetime import date
now = date.today()
print(now)
print('两数之和：%.f' % (float(input('请输入第一个数字：')) + float(input('请输入第二个数字：'))))

