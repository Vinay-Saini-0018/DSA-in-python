class Node:
    def __init__(self,val):
        self.val = val
        self.children = []

root = Node(10)
node20 = Node(20)
node30 = Node(30)
node40 = Node(40)
node50 = Node(50)
node60 = Node(60)
node70 = Node(70)
node80 = Node(80)
node90 = Node(90)
node100 = Node(100)

root.children = [node20,node30,node40]
node20.children = [node50,node60,node70]
node30.children = [node80]
node40.children = [node90,node100]

def preorder_traversal(node):
    if not node:
        return None

    print(node.val, end=' ')
    for child in node.children:
        preorder_traversal(child)

def postorder_traversal(node):
    if not node:
        return None
    for child in node.children:
        postorder_traversal(child)

    print(node.val,end=' ')

from collections import deque
def levelorder_traversal(node):
    if not node:
        return None

    q = deque([node])
    while q:
        curr = q.popleft()
        print(curr.val,end=' ')
        for child in curr.children:
            q.append(child)


print('preorder traversal : ')
preorder_traversal(root)
print('\n\npostorder traversal : ')
postorder_traversal(root)
print('\n\nLevelorder traversal : ')
levelorder_traversal(root)