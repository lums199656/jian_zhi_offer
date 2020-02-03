# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        if number == 1:
            return 1
        if number == 2:
            return 2
        pre_1 = 1
        pre_2 = 2
        for i in range(2, number):
            tmp = pre_1
            pre_1 = pre_2
            pre_2 += tmp
        return pre_2


S = Solution()
print(S.jumpFloor(3))
