# Implement a MyQueue class which implements a queue using two stacks.

# Queues use FIFO
import pytest


class Stack:
    def __init__(self):
        self.values = []

    def __repr__(self):
        return "Stack[" + ", ".join(str(v) for v in self.values) + "]"

    def __len__(self):
        return len(self.values)

    def push(self, val):
        self.values.append(val)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.values.pop()

    def is_empty(self):
        return len(self) == 0

    def peek(self):
        if self.is_empty():
            raise ValueError(f"Stack is empty")
        return self.values[-1]


class MyQueue:
    def __init__(self):
        self.stack = Stack()
        self.stack_reversed = Stack()

    def _update_reversed(self):
        while not self.stack.is_empty():
            self.stack_reversed.push(self.stack.pop())

    def add(self, item):
        self.stack.push(item)

    def remove(self):
        if self.stack_reversed.is_empty():
            self._update_reversed()
        return self.stack_reversed.pop()

    def peek(self):
        if self.stack_reversed.is_empty():
            self._update_reversed()
        return self.stack_reversed.peek()

    def is_empty(self):
        return self.stack.is_empty() and self.stack_reversed.is_empty()


# Testing


@pytest.fixture
def queue():
    return MyQueue()


def test_myqueue_add(queue):
    assert queue.is_empty(), "Queue must be empty"
    queue.add(1)
    assert not queue.is_empty(), "Queue cannot be empty after adding"


def test_myqueue_remove(queue):
    queue = MyQueue()
    queue.add(1)
    assert not queue.is_empty(), "Queue cannot be empty after adding"
    removed = queue.remove()
    assert queue.is_empty(), "Queue must be empty after removing single element"
    assert removed == 1, "Wrong element removed"


def test_myqueue_peek(queue):
    assert queue.is_empty(), "Queue cannot be empty after adding"
    queue.add(1)
    assert queue.peek() == 1, "Wrong peek value"
