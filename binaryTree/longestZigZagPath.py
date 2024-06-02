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
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, left, right):
            if not root:
                return
            self.maxDepth = max(self.maxDepth, left, right)
            if root.left and root.left.val:
                dfs(root.left, right+1, 0)
            if root.right and root.right.val:
                dfs(root.right, 0, left+1)
        self.maxDepth = 0
        dfs(root,0,0)
        return self.maxDepth

                
            
root = [1,None,1,1,1,None,None,1,1,None,1,None,None,None,1]
root = [1,1,1,None,1,None,None,1,1,None,1]
tree = BinaryTree(root[0])
for i in range(1, len(root)):
    tree.insert(root[i])
obj = Solution()
result = obj.longestZigZag(tree.root)
print(result)
