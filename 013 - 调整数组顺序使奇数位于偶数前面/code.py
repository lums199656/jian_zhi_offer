# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        even_ = []
        odd_ = []
        for item in array:
            if item % 2 == 0:
                even_.append(item)
            else:
                odd_.append(item)
        return odd_ + even_


S = Solution()
print(S.reOrderArray([1, 2, 3, 4]))
