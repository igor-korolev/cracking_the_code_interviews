# Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might
# topple. Therefore, in real life, we would likely start a new stack when the previous stack
# exceeds some threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks
# should be composed of several stacks and should create a new stack once the previous one
# exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should behave identically to a
# single stack (that is, pop() should return the same values as it would if there were just a
# single stack).
# FOLLOW UP Implement a function popAt(int index) which performs a pop operation on a specific
# sub-stack.


class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.values = []

    def __repr__(self):
        return "Stack" + ", ".join(str(v) for v in self.values) + ""

    def push(self, val):
        if self.is_full():
            raise ValueError("Stack is full")
        self.values.append(val)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.values.pop()

    def is_empty(self):
        return len(self.values) == 0

    def is_full(self):
        return len(self.values) == self.capacity

    def pop_first(self):
        return self.values.pop(0)


class SetOfStacks:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

    def __repr__(self):
        return f"{self.stacks}"

    def __len__(self):
        return sum(len(s.values) for s in self.stacks)

    def push(self, val):
        # If set of stacks is empty or last stack is out of space we create new stack
        if not self.stacks or self.stacks[-1].is_full():
            last_stack = Stack(self.capacity)
            self.stacks.append(last_stack)
        else:
            last_stack = self.last_stack
        last_stack.push(val)

    def pop(self):
        last_stack = self.last_stack

        popped = last_stack.pop()
        if last_stack.is_empty():
            self.stacks.pop()
        return popped

    @property
    def last_stack(self):
        try:
            return self.stacks[-1]
        except IndexError:
            raise IndexError("Set of stacks is empty")

    def pop_at(self, ind):  # This is the follow up
        try:
            stack = self.stacks[ind]
        except IndexError:
            raise IndexError(f"Stack with index {ind} is not found")

        popped = stack.pop()
        if stack.is_empty():
            del self.stacks[ind]
        else:
            # we need to shift all stacks next to the popped one to fill the gaps
            self.shift_left(ind)
            if self.last_stack.is_empty():  # if the last stack becomes empty after shifting
                self.stacks.pop()
        return popped

    def is_empty(self):
        return len(self.stacks) == 0

    def shift_left(self, stack_index):
        for i in range(stack_index, len(self.stacks) - 1):
            current_stack = self.stacks[i]
            next_stack = self.stacks[i + 1]
            if not current_stack.is_full():
                current_stack.push(next_stack.pop_first())


def test_set_of_stacks_is_empty():
    set_stacks = SetOfStacks(2)
    assert set_stacks.is_empty() is True, "Set of stacks must be empty"


def test_set_of_stacks_push():
    set_stacks = SetOfStacks(2)
    set_stacks.push(100)
    last_stack = set_stacks.last_stack
    assert 100 in last_stack.values, "Value is not added to last stack of set"

    # Checking mechanism of inner creation of stacks in a set
    set_stacks.push(200)
    set_stacks.push(300)
    assert len(set_stacks.stacks) == 2, (
        "Must be two inner stacks after pushing 3 elements in " "2-capacity set"
    )


def test_set_of_stacks_pop():
    set_stacks = SetOfStacks(2)
    set_stacks.push(100)
    last_stack = set_stacks.last_stack
    assert not last_stack.is_empty()

    set_stacks.pop()
    assert last_stack.is_empty(), "After popping out element stack has to be empty"


def test_set_of_stacks_pop_at():
    set_stacks = SetOfStacks(2)
    set_stacks.push(100)
    set_stacks.push(200)
    set_stacks.push(300)

    set_stacks.pop_at(0)  # 200 should be popped out
    assert set_stacks.last_stack.values == [100, 300], (
        "After popping out at zero index " "first and stacks should be merged"
    )
    assert len(set_stacks.stacks) == 1, "Last empty stack has to be deleted"
