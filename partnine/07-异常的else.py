num = 12
try:
    print(num)
except Exception as result:
    print(result)
else:
    print('我是else，没有异常要执行')
# 输出
# 12
# 我是else，没有异常要执行