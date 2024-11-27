# The largestValues method finds the largest value in each row of a binary tree.

# Step 1: Initialization
#   - If the tree is empty, return an empty list.
#   - Use a queue (deque) to perform level-order traversal, starting with the root node.

# Step 2: Level-Order Traversal
#   - For each level, initialize 'row_max' to track the largest value.
#   - Iterate through all nodes in the current level:
#       - Update 'row_max' with the maximum value.
#       - Add left and right children to the queue for the next level.
#   - Append 'row_max' to the result list.

# Step 3: Return Result
#   - Return 'res', containing the largest values for each row.

# TC: O(n) - Each node is visited once.
# SC: O(n) - Space for the queue during traversal.


from collections import deque
from typing import List, Optional


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        q = deque([root])
        while q:
            row_max = q[0].val
            length = len(q)
            for i in range(length):
                node = q.popleft()
                row_max = max(row_max, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(row_max)

        return res
