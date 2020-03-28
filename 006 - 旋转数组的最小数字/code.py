# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        min_ = min(rotateArray)
        return min_
        # index = rotateArray.index(min_)
        # ret = rotateArray[index:] + rotateArray[:index]
        # print(ret)
        # return ret


S = Solution()
S.minNumberInRotateArray([3, 4, 5, 1, 2])
