"""
    在python中，一共有两种循环结构   while   for
    场景：
        for循环适合对数据容器（列表、元组、字典、集合、字符串）进行遍历

    for 语法：
        for 临时变量 in 数据容器        # 把数据容器拆开了，一个一个赋值给临时变量      从右往左看
            ①：首先自动判断数据容器中有多少个元素，有多少个元素，就循环几次
            ②：每次循环时，系统会自动的将结果放入临时变量（临时变量=结果）输出临时变量
            执行缩进体内的代码


for循环主要用来遍历容器

"""


i = "isjdisajd"
for a in i:
    print(a)
    if a == "a":
        break

