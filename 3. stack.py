# Data Structure: Stack
# Stack implementation using list
# Stack is a linear data structure which follows a particular order in which the operations are performed. 
# The order may be LIFO(Last In First Out) or FILO(First In Last Out). 

# Mainly the following three basic operations are performed in the stack:
# Push: Adds an item in the stack. If the stack is full, then it is said to be an Overflow condition.  
# Pop: Removes an item from the stack. The items are popped in the reversed order in which they are pushed.
# If the stack is empty, then it is said to be an Underflow condition.
# Peek or Top: Returns top element of stack.

stack_list = []

# Push
stack_list.append("a")

# Push
stack_list.append("b")

# Push
stack_list.append("c")

# Pop
stack_list.pop()

# Peek
print(stack_list[-1])

# Output: b
# Time Complexity:
# push(), pop(), peek() and isEmpty() all take O(1) time.