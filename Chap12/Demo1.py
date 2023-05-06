#1. 类的创建

class Student:  # Student为类名，由一个或者多个单词组成，要求每个单词首字母大写，其余小写
    native_place = '吉林'  # 直接写在类中的变量，称为类属性

    # 初始化方法
    def __init__(self, name, age):
        self.name = name  # self.name为实例属性，进行了赋值操作，将局部变量name的值赋值给实体属性
        self.age = age

    # 实例方法（在类之外定义的是函数，在类之内定义的是方法）
    def eat(self):
        print('学生在吃饭')

    # 静态方法
    @staticmethod
    def method():  # 不写self,不允许写self
        print('我使用了静态方法')

    # 类方法
    @classmethod
    def cm(cls):
        print('我使用了类方法')


# python中一切皆对象，student是对象吗？有开空间吗
print(id(Student))
print(type(Student))
print(Student)


# 函数
def drink():
    print('喝水')