"""
This module provides implementation of Queue and MinHeap data structures.

These data structures are essential for algorithmic operations, such as search algorithms. The Queue class implements
a standard FIFO (First In, First Out) queue, while the MinHeap class provides a min-heap for efficient priority queue
operations.

Author: Peyman Kh
Date: 06/Feb/2024
"""


class Queue:
    """Queue data structure implementation."""

    def __init__(self):
        """Initializing the queue."""
        self.queue = []

    def enqueue(self, value):
        """
        Adds an element to the end of the queue.

        Parameters:
            - value (any): The value to be added to the queue.

        Returns:
            - None
        """
        self.queue.append(value)

    def dequeue(self):
        """
        Removes and returns the element from the front of the queue.

        Returns:
            - any: The element at the front of the queue, or None if the queue is empty.
         """
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def peek(self):
        """
        Returns the element at the front of the queue without removing it.

        Returns:
            - any: The element at the front of the queue.
        """
        return self.queue[0]

    def is_empty(self):
        """
        Checks whether the queue is empty.

        Returns:
            - bool: True if the queue is empty, False otherwise.
        """
        return len(self.queue) == 0


class MinHeap:
    """Implements a min-heap for efficient minimum value retrieval and priority queue operations."""
    def __init__(self):
        """Initialize an empty min-heap."""
        self.heap = []

    def push(self, value):
        """
        Inserts a new element into the min-heap, maintaining the heap property.

        Parameters:
            - value (any): The value to be added to the min-heap.

        Returns:
            - None
        """
        self.heap.append(value)  # Append the new element to the end of the heap
        self._heapify_up(len(self.heap) - 1)  # Ensure the heap property is maintained

    def pop(self):
        """
        Removes and returns the smallest element from the min-heap, maintaining the heap property.

        Returns:
            - any: The smallest element from the min-heap, or None if the heap is empty.
        """
        if not self.heap:
            return None  # Heap is empty

        if len(self.heap) == 1:
            return self.heap.pop()  # Only one element in the heap

        top_value = self.heap[0]  # Store the smallest item to return
        self.heap[0] = self.heap.pop()  # Move the last element to the top and remove the last
        self._heapify_down(0)  # Ensure the heap property is maintained from the top down

        return top_value

    def _heapify_up(self, index):
        """
        Move the item at the given index up to its correct position.

        Parameters:
            - index (int): The index of the element to heapify up.

        Returns:
            - None
        """

        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            self._swap(index, parent_index)
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        """
        Move the item at the given index down to its correct position.

        Parameters:
            - index (int): The index of the element to heapify down.

        Returns:
            - None
        """
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self._swap(index, smallest)
            self._heapify_down(smallest)

    def _swap(self, i, j):
        """
        Swap the items at the given indices.

        Parameters:
            - i (int): The index of the first element to swap.
            - j (int): The index of the second element to swap.

        Returns:
            - None
        """
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def is_empty(self):
        """
        Checks whether the min-heap is empty.

        Returns:
            - bool: True if the min-heap is empty, False otherwise.
        """
        return len(self.heap) == 0
