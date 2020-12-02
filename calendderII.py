class Node:
    def __init__(self, start, end):
        self.val = (start, end)
        self.left = None
        self.right = None

    def insert(self, start, end):
        if self.val[0] >= end:
            if not self.left:
                self.left = Node(start, end)
                return True
            return self.left.insert(start, end)
        elif self.val[1] <= start:
            if not self.right:
                self.right = Node(start, end)
                return True
            return self.right.insert(start, end)


class Solution:
    def __init__(self):
        self.root = None

    def book(self, start, end):
        if not self.root:
            self.root = Node(start, end)
            return True
        return self.root.insert(start, end)


exam1 = Solution()
exam1.book(4, 5)
exam1.book(1, 4)
exam1.book(5, 7)
print()
