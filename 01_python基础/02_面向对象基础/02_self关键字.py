"""
    self（自身的,自己的） 关键字：
        概述：
            代表本类当前对象的引用，谁（哪个对象）调用，self就代表谁
        作用：
            用于实现函数[区分不同对象]的
        总结：大白话
            1.如果你是c1对象，那么self值，代表c1，如果c2调用，self值就代表c2
            2.函数内部都有一个self，哪个对象调用，self就代表谁

    self 是 python内置的关键字，用于指向对象实例本身

    self的常见作用：
        在类的内部调属性和方法
        self可以用来区分不同对象

    总结： 在类内 和 类外方法的调用
        1.在类内，访问类中的行为（函数），通过 self.的方式进行访问
        2.在类外，访问类中的行为（函数），通过对象名.函数进行访问

    在Python中，定义在类中的方法的第一个参数通常是self。
        这是一个约定，用于表示方法所属的实例对象。
        通过self，方法可以访问实例的属性和其他方法。

"""


# 类的调用
class Car:
    # 属性 和 行为
    def run(self):
        print(f"{self}跑起来了")

# 2.类的调用
c1 = Car()
print(f"c1对象：{c1}")     # <__main__.Car object at 0x000001E6D2C04140>
c1.run()                  # <__main__.Car object at 0x000001E6D2C04140>


print("♥"*50)

c2 = Car()
print(f"c2对象：{c2}")     # <__main__.Car object at 0x000001E6D2C04170>
c2.run()                  # <__main__.Car object at 0x000001E6D2C04170>

# 小结： c1和c2打印的值不同，因为他们是不同的对象，self代表的是c1 和 c2




