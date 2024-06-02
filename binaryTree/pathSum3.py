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
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        def dfs(root, flag, residual):
            if not root:
                return
            if root.val == None:
                return
            residual -= root.val
            if residual == 0:
                self.count += 1
            dfs(root.left, False, residual)
            dfs(root.right, False, residual)
            if flag:
                dfs(root.left, True, self.targetSum)
                dfs(root.right, True, self.targetSum)
        self.targetSum = targetSum
        self.count = 0
        dfs(root, True, self.targetSum)
        return self.count

root = [10,5,-3,3,2,None,11,3,-2,None,1]
targetSum = 8
tree = BinaryTree(root[0])
for i in range(1, len(root)):
    tree.insert(root[i])
obj = Solution()
result = obj.pathSum(tree.root,targetSum)
print(result)
