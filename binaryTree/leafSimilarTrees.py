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
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def findLeaf(root):
            leftLeaf = []
            rightLeaf = []
            if root.left == None and root.right == None:
                if root.val == None:
                    return []
                else:
                    return [root.val]
            if root.left.val == None and root.right.val == None:
                if root.val == None:
                    return []
                else:
                    return [root.val]
            if root.left != None:
                leftLeaf = findLeaf(root.left)
            if root.right != None:
                rightLeaf = findLeaf(root.right)
            return leftLeaf + rightLeaf
        leafs1 = findLeaf(root1)
        leafs2 = findLeaf(root2)       
        return leafs1 == leafs2
      
root1 = [3,5,1,6,2,9,8,None,None,7,4]
root2 = [3,5,1,6,7,4,2,None,None,None,None,None,None,9,8]
tree1 = BinaryTree(root1[0])
for i in range(1, len(root1)):
    tree1.insert(root1[i])
tree2 = BinaryTree(root2[0])
for i in range(1, len(root2)):
    tree2.insert(root2[i])
obj = Solution()
result = obj.leafSimilar(tree1.root, tree2.root)
print(result)
