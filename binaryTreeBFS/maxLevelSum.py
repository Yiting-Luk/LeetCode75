import numpy as np
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BinaryTree:
    def __init__(self, val):
        self.root = TreeNode(val) 
    def insert(self, val):
        node = TreeNode(val)
        if self.root == None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            curr_node = queue.pop(0)
            if curr_node.left == None:
                curr_node.left = node
                break
            else:
                if curr_node.left.val != None:
                    queue.append(curr_node.left)                
            if curr_node.right == None:
                curr_node.right = node
                break
            else:
                if curr_node.right.val != None:
                    queue.append(curr_node.right)

class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, level):
            if root:
                kids = []
                if root.left:
                    if root.left.val != None:
                        kids.append(root.left.val)
                    else:
                        kids.append(0)
                if root.right:
                    if root.right.val != None:
                        kids.append(root.right.val)
                    else:
                        kids.append(0)
                sumKids = sum(kids)
                if len(self.levelSum) == level:
                    self.levelSum.append(sumKids)
                else:
                    self.levelSum[level] += sumKids
            if root.left:
                dfs(root.left, level+1)
            if root.right:
                dfs(root.right, level+1)
        self.levelSum = [root.val]
        level = 1
        dfs(root, level)
        self.levelSum.pop(-1)
        # return np.argmax(self.levelSum)+1
        return self.levelSum


root = [1,7,0,7,-8,None,None]
root = [-100,-200,-300,-20,-5,-10,None]
tree = BinaryTree(root[0])
for i in range(1, len(root)):
    tree.insert(root[i])
obj = Solution()
result = obj.maxLevelSum(tree.root)
print(result)