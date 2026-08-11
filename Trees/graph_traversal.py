from collections import deque

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


A = TreeNode('A')
B = TreeNode('B')
C = TreeNode('C')
D = TreeNode('D')
E = TreeNode('E')
F = TreeNode('F')

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F

class Traversal:
    def preorder(node):
        if not node:
            return

        print(node.val,end=' ')
        Traversal.preorder(node.left)
        Traversal.preorder(node.right)

    def inorder(node):
        if not node:
            return
        Traversal.inorder(node.left)
        print(node.val,end=' ')
        Traversal.inorder(node.right)

    def postorder(node):
        if not node:
            return
        Traversal.postorder(node.left)
        Traversal.postorder(node.right)
        print(node.val,end=' ')

    def levelorder(node):
        if not node:
            return
        
        q = deque([node])
        while q:
            curr = q.popleft()
            print(curr.val,end=' ')

            if curr.left:
                q.append(curr.left)
            
            if curr.right:
                q.append(curr.right)

        
            

print("preorder traversal : ")
Traversal.preorder(A)
print("\n\ninorder traversal : ")
Traversal.inorder(A)
print("\n\npostorder traversal : ")
Traversal.postorder(A)
print("\n\nlevelorder traversal : ")
Traversal.levelorder(A)