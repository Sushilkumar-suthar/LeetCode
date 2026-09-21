# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if root == None:
            return True

        s1,s2 = [],[]

        s1.append(root.left)
        s2.append(root.right)

        while s1 and s2:
            n1 = s1.pop()
            n2 = s2.pop()

            if n1 is None and n2 is None:
                continue
            
            if n1 is None or n2 is None or n1.val!=n2.val:
                return False

            s1.append(n1.left)
            s2.append(n2.right)

            s1.append(n1.right)
            s2.append(n2.left)

        return len(s1) == 0 and len(s2)==0
