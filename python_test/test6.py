'''
print('{}网站:"{}!"'.format('菜鸟教程', 'www.runbook.com'))
print('站点列表：{}，{}，{other}'.format('google', 'baidu', other='runbook'))
print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob', other='Taobao'))
import math
print('PI的近似值:{0:.3F}'.format(math.pi))
print("你输入的是:", input("请随便输入"))
'''
# 打开一个文件
f = open("C:/Users/song/Desktop/song.txt", "r")

#str = f.readlines()
#print(str)
for line in f:
    print(line, end='')
# 关闭打开的文件
f.close()
