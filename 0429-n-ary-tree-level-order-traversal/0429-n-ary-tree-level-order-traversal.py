"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
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
                print(node.val)
                for child in node.children:
                    q.append(child)

            current_level +=1

        return result