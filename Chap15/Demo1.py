import os

os


file1 = open('c.txt', 'a')

lst = ['java', 'go', 'python']
file1.write('中国')  # 将字符串内容写入文件
file1.writelines(lst)  # 将列表内容写入文件
print('testname',file1.name)
file1.close()