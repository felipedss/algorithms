# data-structure

## Install black formatter

```bash
pip install black
```

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

---

## Queue

The queue follows the FIFO (First in - First out) structure where the first element inserted would be the first element deleted. It's like a line of people waiting the bus.

Queues can be implemented with either an array or a linked list (with tail pointer).
For array we have a maximum size, and for linke-lists we don't.
But, for linked-lists we've got the overhead of storing a pointer as well.

- Enqueue = O(1)
- Dequeue = O(1)
- isEmpty = O(1)

### Arrays

[Implementation](python/queue/queue_array.py)

### Fixed-sized array

[Pending to implement]

### LinkedLists

[Pending to implement]

---

## Hash Table

Hash tables represents a dynamic set of data for INSERT, DELETE and SEARCH

Where hash table really shine is search:

- Average: O(1)
- Worse case O(n))

Hash table sometimes is used interchangeably with dictionary.

```python
dictionary = {
    'a': 1,
    'b': 9,
    'c': 'nebraska',
    'd': True
}
```

- Dictionary = generic way to MAP keys to values
- Hash table = implementation of a dictionary using a hash function

With hash table we introduce **hash-functions** that maps keys to a location in the table that holds data.

When two different hash functions (keys) points to the same data in the hash table, we called that as collision.

How to acomoddate collisions: Through **chaining**

![img](img/hash-table-collision.png)

To support chaining we introduce linked lists and our table locations become a bucket of values.

### Hash function goals

- Goals

  - Maximizes randomness
  - Produces the least amount of colisions

- Examples

  - division
  - multiplication
  - universal hashing
  - dynamic perfect hashing

### Hash by division

This is one of the simplest ways to create a hash function, although it may not be the most efficient in all cases.

```python
def hashing_by_division(k, m):
    return k % m

k = 50
m = 13
print(f'hash of 50 with table size 13 --> {hashing_by_division(k, m)}') # The hash value here is 11
```

- [See more here - Code](python/queue/queue_array.py)
- [Source - Youtube link](https://www.youtube.com/watch?v=knV86FlSXJ8)
