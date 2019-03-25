# _*_coding:utf-8_*_

# 创建用户  ：chenzhengwei

# 创建日期  ：2019/3/25 下午2:24


def insert_sort(list_data):
    for i in range(1,list_data.__len__()):
        tem = list_data[i]
        for j in range(i):
            if tem < list_data[j]:
                list_data[i],list_data[j] = list_data[j],list_data[i]


if __name__ == '__main__':
    list_data = [1,2,3,4]
    insert_sort(list_data)
    print(list_data)