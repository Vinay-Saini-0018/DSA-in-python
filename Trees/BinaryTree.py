class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

def insert(root,key):
    if not root:
        return TreeNode(key)

    if key<root.val:
        root.left = insert(root.left,key)

    else:
        root.right = insert(root.right,key)

    return root


def search(node,key):
    if not node:
        return False
    if node.val == key:
        return True
    
    if key < node.val:
        return search(node.left,key)

    return search(node.right,key)

def deletion(node,key):
    if not node:
        return None

    if key<node.val:
        node.left = deletion(node.left,key)
    elif key>node.val:
        node.right  = deletion(node.right,key)
    # deletion node found
    else:
        if not node.left:
            return node.right

        if not node.right:
            return node.left

        while succ.left:
            succ = succ.left

        node.val = succ.val
        node.right = deletion(node.right,succ.val)

    return node

bst = BST()
root = insert(bst.root,5)
root = insert(root,6)
root = insert(root,7)
root = insert(root,8)
root = insert(root,9)
root = insert(root,4)
root = insert(root,3)
root = insert(root,2)

print(search(root,3))
print(deletion(root,2))