# _*_ coding=utf-8 _*_


import numpy as np

"""
通用函数：
        能同时对数组中所有元素进行运算的函数
    一元函数：abs,sqrt,ceil,floor,rint,trunc,modf,isnan,isinf,    
    二元函数：add,substract,multiply,divide,power,mod,maximum,minimum
"""
arr = np.arange(-5, 2, 0.5)
print(arr)
# sqrt开方
print(np.sqrt(arr))
# ceil 向上取整
print(np.ceil(arr))

# floor 向下取整
print(np.floor(arr))

# trunc 取整数部分
print(np.trunc(arr))

# rint 四舍五入
print(np.rint(arr))

# isnan, 判断数组中的元素是否是nan，nan指不存在的数，比如5/
# nan常被用来表示数据缺失值
b = np.arange(5)
# c = b/b
# print(c)
# print(np.isnan(c))

# isinf ，判断数组中元素是否为inf，inf为无限大的数

"""二元函数：传入两个参数"""
# maximum将两个数组每个元素进行比较，取出较大的
c = np.arange(5)
d = np.array([2, 4, 56, 6, 77])
print(np.maximum(c, d))

# minimum将两个数组每个元素进行比较，取出较小的
print(np.minimum(c, d))
