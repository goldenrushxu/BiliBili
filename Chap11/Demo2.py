#2. 知识点不熟导致的错误



lst = [11, 22, 33, 44]
print(lst[3])  # 4越界，从0开始

lst1 = []
# lst1.append('A', 'B', 'c')
lst1.append('A')
lst1.append('B')
lst1.append('C')  # 一次一个
lst1.extend(['a','b','c'])
print(lst1)