#13. 类的赋值与浅深拷贝



class CPU:
    pass


class Disk:
    pass


class Computer:
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk


# 变量的赋值
cpu1 = CPU()
cpu2 = cpu1
print(cpu1, id(cpu1))
print(cpu2, id(cpu2))  # 内存地址相同，同一个对象，放到两个地址中存储，形成两个变量

# 浅拷贝：一般都是浅拷贝，拷贝时，对象包含的子对象内容不拷贝，因此源对象与拷贝对象会引用同一个子对象
disk1 = Disk()
computer = Computer(cpu1, disk1)

import copy
computer2 = copy.copy(computer)
print(computer, computer.cpu, computer.disk)
print(computer2, computer2.cpu, computer2.disk)

# 深拷贝：使用copy模块的deepcopy函数，递归拷贝对象中包含的子对象，源对象和拷贝对象所有的子对象也不相同
computer3 = copy.deepcopy(computer)
print(computer, computer.cpu, computer.disk)
print(computer3, computer3.cpu, computer3.disk)