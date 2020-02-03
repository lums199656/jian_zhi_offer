# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number <= 0:
            return 0
        else:
            number = number - 1
            return pow(2, number)


S = Solution()
print(S.jumpFloorII(2))