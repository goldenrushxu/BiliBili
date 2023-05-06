#5. 常见的异常类型


# 1.除（或取模）零 所有数据类型
# print(10/0)  # ZeroDivisionError

# 2.序列中没有此索引
lst = [11, 22, 33, 44]
# print(lst[4])  # IndexError

# 3.映射中没有这个键
dic = {'name': '张三', 'age': 20}
# print(dic['gender'])  # KeyError

# 4.未声明/初始化对象（没有属性）
# print(num)  # NameError

# 5.语法错误
# int a=20  # SyntaxError

# 6.传入无效的参数
# a = int('hello')  # ValueError