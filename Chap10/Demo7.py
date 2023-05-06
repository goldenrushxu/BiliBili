def fun(a, b):
    c = a * b  # c为局部变量，因为c在函数体内进行定义的变量，ab为函数的形参，作用范围也是函数内部，相当于局部变量
    print(c)


# print(a, c)  # 因为a和c超出了起作用的范围（超出了作用域）


name = '杨老师'
print(name)


def fun2():
    print(name)


fun2()  # name的作用范围为函数的内部和外部都可以使用，称为全局变量


def fun3():
    global age  # 函数内部定义的变量，局部变量，局部变量可以使用global进行生命，这个变量实际上就变成了全局变量
    age = 20
    print(age)


fun3()
print(age)