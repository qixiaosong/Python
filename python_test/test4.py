#import time
#print("time:", time.time())
#print("获取当地时间：", time.localtime(time.time()))
#print("获取可读当地时间：", time.asctime(time.localtime(time.time())))
#print(time.strftime("%Y-%m-%d %H:%M:%S %A %p %w %x", time.localtime()))
import calendar
print("输出2016年1月份的日历：", calendar.month(2016, 1))
