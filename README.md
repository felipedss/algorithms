# data-structure

## Big O notation

- Cheat Sheet: https://flexiple.com/algorithms/big-o-notation-cheat-sheet/
- Video: https://www.youtube.com/watch?v=v4cd1O4zkGw

---

## Array

### Contiguous area of memory

- Random access
- Constant time access to any particular element in an array (read and write)

### Times for commons operations

- Adding at the end: O(1)
- Removing at the end: O(1)

- Adding at the beginning: O(n)
- Removing at the beginning: O(n)

- Adding at the middle: O(n)
- Removing at the middle: O(n)

Arrays are great if you want to add or remove at the end. But, expensive if you want to add or remove in the middle or at the beginning

**Huge advantage:** Constant time to access elements.

---

## LinkedList

A LinkedList is a linear data structure in which elements are stored in nodes. Each node contains a value and a pointer that points to the next node in the sequence. In this way, elements are organized sequentially, but not necessarily in contiguous memory positions.

| Singly-Linked List | no tail | with tail |
| ------------------ | ------- | --------- |
| push_front         | O(1)    |           |
| top_front          | O(1)    |           |
| pop_front          | O(1)    | O(1)      |
| push_back          | O(n)    | O(1)      |
| top_back           | O(n)    | O(1)      |

---

## Stack

The stack follows the LIFO (Last in - First out) structure where the last element inserted would be the first element deleted. It's like a stack of books.

- Adding an element = O (1)
- Removing an element = O (1)

Stacks can be implemented with either an array or a linked list:

### Arrays - [Stack array implementation](python/stack/stack_array.py)

Disadvantage of arrays: you've potentially over-allocated.

### LinkedLists - [PENDING TO IMPLEMENT]

For array we have a maximum size, and for linke-lists we don't.
But, for linked-lists we've got the overhead of storing a pointer as well.

### Most common algorithm:

- Balanced brackets
