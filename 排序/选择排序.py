# _*_coding:utf-8_*_

# 创建用户  ：chenzhengwei

# 创建日期  ：2019/3/14 下午10:25


def select_sort(list_data):
    for i in range(list_data.__len__() - 1):
        min_value_index = i
        for j in range(i + 1, list_data.__len__()):
            if list_data[j] < list_data[min_value_index]:
                min_value_index = j
        list_data[i], list_data[min_value_index] = list_data[min_value_index], list_data[i]


if __name__ == '__main__':
    list_data = [2, 1, 3, 2, 2, 2]
    select_sort(list_data)
    print(list_data)
