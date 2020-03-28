# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        if n == 1:
            return 1
        pre_1 = 0
        pre_2 = 1
        for i in range(2, n + 1):
            tmp = pre_1
            pre_1 = pre_2
            pre_2 += tmp
        return pre_2


S = Solution()
print(S.Fibonacci(6))
