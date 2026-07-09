# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None: return []

        q = []
        result = []

        q.append(root)
        current_level = 0

        while q:
            len_q = len(q)
            result.append([])
            
            for _ in range(len_q):
                node = q.pop(0)
                result[current_level].append(node.val)

                if node.left:q.append(node.left)
                if node.right:q.append(node.right)

            current_level +=1

        return result[::-1]