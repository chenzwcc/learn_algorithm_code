# _*_coding:utf-8_*_

# 创建用户  ：chenzhengwei

# 创建日期  ：2019/5/5 下午2:14


"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution.
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution(object):
    def __init__(self, target_list, target_value):
        self.hashdict = {}
        self.target_list = target_list
        self.target_value = target_value

    def get_target_index(self):
        for key, value in enumerate(self.target_list):
            self.hashdict[key] = value

        for value in range(len(self.hashdict.values())):
            for j in range(value, len(self.hashdict.values())):
                if self.target_value - list(self.hashdict.values())[value] == list(self.hashdict.values())[j]:
                    return [value, j]
        return [-1, -1]


if __name__ == '__main__':
    solution = Solution(target_list=[5, 3, 4, 5, 6, 5, 6, 11, 32], target_value=11)
    print(solution.get_target_index())
