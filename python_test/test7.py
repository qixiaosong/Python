'''
i = 7
print("输出整型：%d,输出浮点型：%f" % (i, i))
'''


class people:
    name = ''
    age = 0
    __weight = 0

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self._weight = w

    def speak(self):
        print("%s说:今年我%d岁了" % (self.name, self.age))
p = people('song', 21, 139)
p.speak()


class student(people):
    grade = ''

    def __init__(self, n, a, w, g):
        people.__init__(self, n, a, w)
        self.grade = g

    def speak(self):
        print("%s说:今年我%d岁了,在上%d年级。" % (self.name, self.age, self.grade))
s = student('song', 21, 139, 1)
s.speak()


class speaker():
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我是%s，我是一位演讲家，今天我的演讲主题是：%s" % (self.name, self.topic))


class sample(speaker, student):
    a = ''

    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, g, w)
        speaker.__init__(self, n, t)

test = sample('song', 21, 139, 3, 'python')
test.speak()


class Parent:        # 定义父类

    def myMethod(self):
        print('调用父类方法')


class Child(Parent):  # 定义子类

    def myMethod(self):
        print('调用子类方法')

c = Child()          # 子类实例
c.myMethod()         # 子类调用重写方法
p = Parent()
p.myMethod()


class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0    # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print (self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
print (counter.publicCount)
print (counter.__secretCount)  # 报错，实例不能访问私有变量


