# _*_coding:utf-8_*_

# 创建用户  ：chenzhengwei

# 创建日期  ：2019/3/25 下午3:00


def partition(list_data, left_index, right_index):
    tem = list_data[left_index]
    while left_index < right_index:
        while left_index < right_index and tem <= list_data[right_index]:
            right_index -= 1
        list_data[left_index] = list_data[right_index]
        while left_index < right_index and tem >= list_data[left_index]:
            left_index += 1
        list_data[right_index] = list_data[left_index]
    list_data[left_index] = tem
    return left_index


def quick_sort(list_data, left_index, right_index):
    if left_index < right_index:
        middle_index = partition(list_data, left_index, right_index)
        quick_sort(list_data, left_index, middle_index - 1)
        quick_sort(list_data, middle_index + 1, right_index)


if __name__ == '__main__':
    list_data = [1, 2, 3, 2, 6, 7, 2, 1]
    quick_sort(list_data, 0, len(list_data) - 1)
    print(list_data)
