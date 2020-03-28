# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        bin_ = str(bin(n))
        print(bin_)
        if bin_[0] == '-':
            print(str(bin_[3:]))
        else:
            print(str(bin_[2:]))


S = Solution()
S.NumberOf1(3)
