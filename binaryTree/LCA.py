# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
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
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        if left or right:
            return left or right
        
root = [3,5,1,6,2,0,8,None,None,7,4]
p = 5
q = 1
tree = BinaryTree(root[0])
for i in range(1, len(root)):
    tree.insert(root[i])
p = tree.root.left
print(p.val)
q = tree.root.right
print(q.val)
obj = Solution()
result = obj.lowestCommonAncestor(tree.root, p, q)
print(result.val)