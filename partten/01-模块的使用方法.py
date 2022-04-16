# import math
#
# print(math.sqrt(9))

# 方法二 ： from 模块名 import 功能1, 功能2 （不需要书写模块名.功能名）
# from math import sqrt
# print(sqrt(9))


#方法三 ： from 模块名 import *
# from math import *
# print(sqrt(9))


# 方法四
# import 模块名 as 别名
# from 模块名 import  功能 as 别名
import time as te

te.sleep(2)
print('hello')

from time import sleep as sl
sl(2)
print('python')