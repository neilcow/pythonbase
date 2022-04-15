try:
    print(num)
except(NameError, ZeroDivisionError) as result:
    print(result)
    
# 输出 name 'num' is not defined