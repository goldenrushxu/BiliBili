#6. traceback模块的使用

# print(10/0)
import traceback

try:
    print('-------------')
    print(1 / 0)
except:
    traceback.print_exc()