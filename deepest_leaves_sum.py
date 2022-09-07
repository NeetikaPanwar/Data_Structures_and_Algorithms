# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import operator


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        leaves_sum = 0
        height_val = dict()
        max_height = 0
        level = 0

        def get_deep_sum(root, level, max_height, height_val):

            if not root:
                return 0

            lh = get_deep_sum(root.left, level + 1, max_height, height_val)
            rh = get_deep_sum(root.right, level + 1, max_height, height_val)

            if lh == 0 and rh == 0:
                height = level

                if height >= max_height:
                    if height in height_val:
                        height_val[height].append(root.val)
                    else:
                        height_val[height] = [root.val]

                    max_height = height

            return 1 + max(lh, rh)

        get_deep_sum(root, 1, max_height, height_val)

        sorted_h_val = sorted(height_val.items(), key=operator.itemgetter(0), reverse=True)

        i = 0
        for h, vals in sorted_h_val:
            if i == 0:
                for v in vals:
                    leaves_sum += v
                break
            i += 1
        return leaves_sum