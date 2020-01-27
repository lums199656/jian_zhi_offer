def printListFromTailToHead(listNode):
    root = listNode
    ret = []
    while root is not None:
        ret.insert(0, root.val)
        root = root.next
    return ret


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
