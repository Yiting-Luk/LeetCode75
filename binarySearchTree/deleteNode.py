# A Binary Search Tree is a data structure used in computer science for organizing and storing data in a sorted manner. 
# Each node in a Binary Search Tree has at most two children. 
# The left child contains values less than the parent node.
# The right child contains values greater than the parent node.

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
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return root
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right:
                root = None 
                # If there's no left or right subtree we found the leaf. 
                # Delete this node without any further traversing.
            elif root.right:
                root.val = self.successor(root) 
                # Found the key of minimum from the right subtree
                root.right = self.deleteNode(root.right, root.val)
                # replace the delete node with the minimum from the right subtree such that it is still a BST
            else:
                root.val = self.predecessor(root)
                # Found the key of maximum from the left subtree
                root.left = self.deleteNode(root.left, root.left.val)
                # replace the delete node with the maximum from the left subtree           
        return root
    def successor(self, root):
        root = root.right
        while root.left:
            root = root.left
        return root.val
    def predecessor(self, root):
        root = root.left
        while root.right:
            root = root.right
        return root.val
root = [5,3,6,2,4,None,7]
root = [2,1]
key = 2
tree = BinaryTree(root[0])
for i in range(1, len(root)):
    tree.insert(root[i])
obj = Solution()
result = obj.deleteNode(tree.root, key)
print(result.val)