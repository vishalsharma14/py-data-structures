# py-data-structures

Python implementation of abstract data structures

## Install
```
pip install py-data-structures
```
## Stack


#### Usage
```
from data_structures import Stack

stack = Stack()
stack.push(item)  # push an item in stack
stack.pop()  # returns the top item from the stack
stack.length  # contains the length of the stack
stack.top  # contains the top item of the stack

stack.iterate()  # override to iterate or perform action on the stack elements
```
#### Exceptions
```
from data_structures import exceptions

# raised on pop() or top when stack is empty
exceptions.EmptyStackException   
```
