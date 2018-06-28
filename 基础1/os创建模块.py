def add (*args):
    print(args)
    sum = 0
    for i in args:
        sum += i
    print(sum)

add(1,2,3,6,7,9)

import datetime
i = datetime.datetime.now()
print ("当前的日期和时间是 %s" % i)
print ("ISO格式的日期和时间是 %s" % i.isoformat() )
print ("当前的年份是 %s" %i.year)
print ("当前的月份是 %s" %i.month)
print ("当前的日期是  %s" %i.day)
print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year) )
print ("当前小时是 %s" %i.hour)
print ("当前分钟是 %s" %i.minute)
print ("当前秒是  %s" %i.second)

import os

print(os.getcwd())
try:
    name = 'abd'
    os.makedirs(name)
    os.chdir('C:\myphp_www\PHPTutorial\Python9523\基础1\%name')

except:
    if os.path.exists('assbc'):
        os.removedirs()
    else:
        while True:
            if os.makedirs('王天官'):
                print('Success')
            break