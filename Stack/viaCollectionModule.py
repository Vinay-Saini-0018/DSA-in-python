# implementing stack using Collections Module

from collections import deque

stack = deque()

# len
print(len(stack))

# display
print(stack)

# is_empty
if len(stack) == 0:
    print("Empty List")

# push
stack.append(4)
stack.append(5)
stack.append(6)
stack.append(7)
stack.append(8)
print(stack)
print(len(stack))

# pop
stack.pop()
stack.pop()
print(stack)

# peek
print(stack[-1])