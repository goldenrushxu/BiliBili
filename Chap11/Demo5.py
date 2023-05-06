#4. 异常处理机制



try:
    a = int(input('请输入第一个整数：'))
    b = int(input('请输入第二个整数：'))
    result = a / b
except BaseException as e:
    print('出错了：', e)
else:
    print('计算结果为：', result)
finally:        #无论是否出错，都会执行
    print('谢谢您的使用')