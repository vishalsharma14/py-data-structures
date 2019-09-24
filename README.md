# py-data-structures

Python implementation of abstract data structures

## Install
```
pip install py-data-structures
```

### Data Structures Covered:
* [Stack](#stack)
* [Queue](#queue)


## Stack


#### Usage
```
from data_structures import Stack

stack = Stack()
stack.push(item)  # push an item in stack
stack.pop()  # returns and removes the top item from the stack
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

## Queue


#### Usage
```
from data_structures import Queue

queue = Queue()
queue.enqueue(item)  # add an item at the end of queue
queue.dequeue()  # returns and removes the first item from the queue
queue.length  # contains the length of the queue
queue.first_item  # contains the first item in the queue
queue.last_item  # contains the last item in the queue

queue.iterate()  # override to iterate or perform action on the queue elements
```
#### Exceptions
```
from data_structures import exceptions

# raised on dequeue(), first_item or last_item when queue is empty
exceptions.EmptyQueueException   
```
