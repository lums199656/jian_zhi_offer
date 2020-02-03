# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        if number == 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        pre_1 = 2
        pre_2 = 3
        for i in range(3, number):
            tmp = pre_1
            pre_1 = pre_2
            pre_2 = tmp + pre_2
        return pre_2


S = Solution()
print(S.rectCover(4))
