# _*_coding:utf-8_*_

# 创建用户  ：chenzhengwei

# 创建日期  ：2019/3/13 下午8:52
import random
from functools import wraps
import time


def onner(func):
    @wraps(func)
    def inner(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print('共花费时间为：%s' % (t2 - t1))
        return result
    return inner


@onner
def bubble_sort(list_data):
    for i in range(list_data.__len__() - 1):
        for j in range(list_data.__len__() - i - 1):
            if list_data[j] > list_data[j + 1]:
                list_data[j], list_data[j + 1] = list_data[j + 1], list_data[j]


# 优化普通冒泡排序
@onner
def bubble_sort2(list_data):
    for i in range(list_data.__len__() - 1):
        flag = False
        for j in range(list_data.__len__() - i - 1):
            if list_data[j] > list_data[j + 1]:
                list_data[j], list_data[j + 1] = list_data[j + 1], list_data[j]
                flag = True
        if not flag:
            break


if __name__ == '__main__':
    list_data = list(range(100))
    print(list_data)
    bubble_sort(list_data)
    bubble_sort2(list_data)

