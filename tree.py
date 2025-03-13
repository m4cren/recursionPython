class TreeNode:
     def __init__(self, value):
          self.value = value
          self.left = None
          self.right = None


def inorder_traversal(root):
     if root:
          inorder_traversal(root.left)
          print(root.value, end = " ")
          inorder_traversal(root.right)  

def preorder_traversal(root):
     if root:
          print(root.value, end=" ")
          preorder_traversal(root.left)
          preorder_traversal(root.right)

def postorder_traversal(root):
     if root:
          postorder_traversal(root.left)
          postorder_traversal(root.right)    
          print(root.value, end = " ")

def preorder_traversal_swap(root):
     if root:


          print(root.value, end = " ")

          swapped = []

          first = preorder_traversal(root.right)
          swapped.append(first)

          second = preorder_traversal(root.left)
          swapped.append(second)

          




root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print('Inorder Traversal')
inorder_traversal(root)

print('\n')
print('Pre-order Traversal')
preorder_traversal(root)

print('\n')
print('Post-order Traversal')
postorder_traversal(root)


print('\n')
print('Pre-order Traversal After Swap')
preorder_traversal_swap(root)
