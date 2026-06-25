# Linked List Problems in Python

A collection of Linked List implementations and problem solutions written in Python.

This repository is part of my Data Structures and Algorithms practice. The goal is to build a strong understanding of linked lists by implementing the data structure from scratch and solving common interview-style problems without relying on built-in containers.

## Features

### Singly Linked List Implementation

* Node creation
* Append
* Prepend
* Insert at position
* Delete by position
* Search
* Traversal
* Length calculation
* String representation

### Linked List Algorithms

Implemented and practiced algorithms include:

* Reverse a linked list
* Reverse a sublist
* Reverse nodes in groups of K
* Find middle node
* Detect cycle (Floyd's Tortoise and Hare)
* Find start of cycle
* Merge two sorted linked lists
* Palindrome linked list check
* Odd-Even node rearrangement
* Random node selection
* Other linked list exercises and variations

## Project Structure

```text
.
├── base.py
├── reverse_list.py
├── palindrome.py
├── cycle_detection.py
├── merge_lists.py
├── ...
```

## Concepts Practiced

* Pointer manipulation
* Fast and slow pointer techniques
* In-place reversal
* Two-pointer algorithms
* Edge-case handling
* Time and space complexity analysis
* Custom data structure implementation

## Sample Node Structure

```python
class Node:
    def __init__(self, value: int):
        self.data = value
        self.next = None
```

## Running the Programs

```bash
python filename.py
```

Example:

```bash
python palindrome.py
```

## Testing Approach

Many solutions were tested using:

* Hand-crafted test cases
* Edge cases
* Randomized input generation
* Multiple repeated executions to verify stability

## Learning Goals

This repository focuses on:

* Understanding linked list internals
* Building intuition for pointer-based algorithms
* Improving problem-solving skills
* Preparing for coding interviews
* Strengthening Python implementation skills

## Future Additions

* Doubly Linked List
* Circular Linked List
* Skip List
* LRU Cache
* Linked List Interview Patterns
* Additional LeetCode and interview problems

## Author

Vishal Kumar

GitHub: https://github.com/Vishal-Kumar-Patel
****