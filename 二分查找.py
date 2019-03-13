# _*_coding:utf-8_*_

# 创建用户  ：chenzhengwei

# 创建日期  ：2019/3/13 下午6:57

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


# 利用二分查找方式查询有序列表中的某一元素,并返回对应的下标
@onner
def bin_search(data_list, val):
    low = 0
    height = data_list.__len__()
    while low <= height:
        mid = int((low + height) // 2)
        if data_list[mid] > val:
            height = mid - 1
        elif data_list[mid] < val:
            low = mid + 1
        else:
            return mid
    return None


if __name__ == '__main__':
    result = bin_search([1, 2, 3, 4, 5, 6, 8], 6)
    print(result)
