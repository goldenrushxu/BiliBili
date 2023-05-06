#继承


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name, self.age)


class Student(Person):
    def __init__(self, name, age, stu_no):
        super().__init__(name, age)     #父类的初始化方法必须写入子类初始化方法中
        self.stu_no = stu_no


class Teacher(Person):
    def __init__(self, name, age, teach_year):
        super().__init__(name, age)      #父类的初始化方法必须写入子类初始化方法中
        self.teach_year = teach_year


stu = Student('张三', 20, '1001')
teacher = Teacher('李四', 34, 10)

stu.info()
teacher.info()


# 多继承
class A(object):
    pass


class B(object):
    pass


class C(B, A):  # 两个父类，多继承
    pass