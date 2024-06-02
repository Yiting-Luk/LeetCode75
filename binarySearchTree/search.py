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
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def dfs(root, val):
            if not root:
                return
            if root.val == val:
                self.subTree = root
                return
            if root.left:
                dfs(root.left, val)
            if root.right:
                dfs(root.right, val)
        self.subTree = None
        dfs(root, val)
        if self.subTree == None:
            return
        else:
            return self.subTree
root = [4,2,7,1,3]
val = 2
tree = BinaryTree(root[0])
for i in range(1, len(root)):
    tree.insert(root[i])
obj = Solution()
result = obj.searchBST(tree.root, val)
print(result.val)
