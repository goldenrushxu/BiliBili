#9. 多态



class Animal(object):
    def eat(self):
        print('动物会吃')


class Dog(Animal):
    def eat(self):
        print('狗吃肉')


class Cat(Animal):
    def eat(self):
        print('猫吃鱼')


class Person(object):
    def eat(self):
        print('人吃五谷杂粮')


def fun(obj):
    obj.eat()


fun(Cat())
fun(Dog())
fun(Animal())
# 不存在继承关系，只关心对象的行为，不关心对象是什么类型
fun(Person())

"""、
静态语言和动态语言关于多态的区别
继承
方法重写
父类引用指向子类对象
"""