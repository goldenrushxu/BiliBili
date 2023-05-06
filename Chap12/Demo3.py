#3. 类属性、类方法、静态方法


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
    def method():  # 不写self
        print('我使用了静态方法')

    # 类方法
    @classmethod
    def cm(cls):
        print('我使用了类方法')


# 类属性的使用方式
print(Student.native_place)
stu1 = Student('张三', 20)
stu2 = Student('李四', 30)
print(stu1.native_place)
print(stu2.native_place)

Student.native_place = '天津'
print(stu1.native_place)
print(stu2.native_place)

# 类方法的使用方式
Student.cm()

# 静态方法的使用方式
Student.method()