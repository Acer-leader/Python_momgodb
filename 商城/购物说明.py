#__author__ = "Alex Li"
#date = 2016/08/22 10:31

#购物车程序
product_list=[
    ('Mac',9000),
    ('kindle',800),
    ('tesla',900000),
    ('python book',105),
    ('bike',2000),
]

salary = 5000
saving = input('请输入你本金：')
shopping_car=[]
if saving.isdigit():
    saving = int(saving)
    while True:
        for i,v in enumerate(product_list,1):
            print(i,v)
        choice = input('选择购买商品编号[退出：q]：')

        if choice.isdigit():
            choice = int(choice)
            if choice > 0 and choice <= len(product_list):
                p_item = product_list[choice - 1]
                if p_item[1] < saving:
                    saving -= p_item[1]
                    shopping_car.append(p_item)
                else:
                    print('余额不足，还剩%s' % saving)
            else:
                print('输入错误')
            print(p_item)

        elif choice == "q":
            print('购买完毕')
            print('您现在所选的商品为：', shopping_car)
            for i in shopping_car:
                print(i)
            print('您还剩%s元钱' % saving)
            break
        else:
            print('invalid input')


