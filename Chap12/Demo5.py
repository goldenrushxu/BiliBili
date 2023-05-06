#5. 封装



class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print('汽车已经启动')


car = Car('宝马')
car.start()
print(car.brand)


class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # age不希望在类的外部使用，所以加了两个__

    def show(self):
        print(self.name, self.__age)


stu = Student('张三', 20)
stu.show()
# 在类的外部使用name与age
print(stu.name)
# print(stu.__age)  # AttributeError
# 怎么在外部使用age
print(dir(stu))  # 打印出来再找
print(stu._Student__age)  # 在类的外部可以通过_Student__age进行访问