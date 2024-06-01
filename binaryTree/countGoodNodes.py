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
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        def dfs(root, curr_max):
            if not root:
                return
            if root.val == None:
                root.val = float('-inf')
            if root.val >= curr_max:
                self.count += 1
                curr_max = root.val
            dfs(root.left, curr_max)
            dfs(root.right, curr_max)
        self.count = 0
        dfs(root, float('-inf'))
        return self.count
root = [3,1,4,3,None,1,5]
tree = BinaryTree(root[0])
for i in range(1, len(root)):
    tree.insert(root[i])
obj = Solution()
result = obj.goodNodes(tree.root)
print(result)