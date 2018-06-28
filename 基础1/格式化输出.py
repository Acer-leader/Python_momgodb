#__author:  Administrator
#date:  2016/8/22

# name = input("Name:")
# age = int(input("Age:"))
# job = input("Job:")
# salary = input("Salary:")
#
# if salary.isdigit(): #长的像不像数字,比如200d , '200'
#     salary = int(salary)
# # else:
# #     #print()
# #     exit("must input digit") #退出程序
#
# msg = '''
# --------- info of %s --------
# Name: %s
# Age : %d
# Job : %s
# Salary: %f
# You will be retired in %s years
# -------- end ----------
# ''' % (name,name ,age ,job ,salary, 65-age )
#
# print(msg)

print('--------------------------------------')
passed_authentication = False
form_name = input('Username:')
pass_word = input('Password:')
if form_name == 'wanghui' and pass_word == '1229129':
    print('信息正确')

else:
    print('信息错误')