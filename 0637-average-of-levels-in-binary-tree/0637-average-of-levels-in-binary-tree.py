# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root == None: return []

        q = []
        result = []

        q.append(root)
        current_level = 0

        while q:
            len_q = len(q)
            r=[]
            
            for _ in range(len_q):
                node = q.pop(0)
                r.append(node.val)

                if node.left:q.append(node.left)
                if node.right:q.append(node.right)

            current_level +=1
            result.append(sum(r)/len(r))

        return result