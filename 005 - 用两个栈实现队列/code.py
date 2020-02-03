# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def push(self, node):
        # write code here
        self.stack_1.append(node)

    def pop(self):
        # return xx
        if not self.stack_2:
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())
        return self.stack_2.pop()

    def __str__(self):
        return ",".join(str(i) for i in self.stack_1)


S = Solution()
S.push(1)
S.push(2)
print(S.pop())
print(S.pop())
print(S)
