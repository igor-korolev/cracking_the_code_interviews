# # Stack Min: How would you design a stack which, in addition to push and pop, has a function min
# # which returns the minimum element? Push, pop and min should all operate in 0(1) time.
from math import inf


class MinStack:
    def __init__(self, stack_size, num_of_stacks=1):
        self.stack_size = stack_size
        self.num_stacks = num_of_stacks
        stack_rows_size = self.stack_size * self.num_stacks
        self.array = [None] * stack_rows_size
        self.sizes = [0] * self.num_stacks
        self.mins = [inf] * stack_rows_size

    def push(self, item, stack_num):
        if self.sizes[stack_num] >= self.stack_size:
            raise ValueError(f"Stack {stack_num} is full")
        self.sizes[stack_num] += 1
        if self.is_empty(stack_num):
            self.mins[self._get_last_position_in_stack(stack_num)] = item
        else:
            self.mins[self._get_last_position_in_stack(stack_num)] = min(
                item, self.mins[self._get_last_position_in_stack(stack_num) - 1]
            )
        self.array[self._get_last_position_in_stack(stack_num)] = item

    def _get_last_position_in_stack(self, stack_num):
        offset = stack_num * self.stack_size
        return offset + self.sizes[stack_num] - 1

    def pop(self, stack_num):
        if self.is_empty(stack_num):
            raise ValueError(f"Stack {stack_num} is empty")
        top_index = self._get_last_position_in_stack(stack_num)
        top_item = self.array[top_index]
        self.array[top_index] = None
        self.sizes[stack_num] -= 1
        return top_item

    def peek(self, stack_num):
        if self.is_empty(stack_num):
            raise ValueError(f"Stack {stack_num} is empty")
        return self.array[self._get_last_position_in_stack(stack_num)]

    def is_empty(self, stack_num):
        return self.sizes[stack_num] == 0

    def min_(self, stack_num):
        return self.mins[self._get_last_position_in_stack(stack_num)]


def test_min():
    stack = MinStack(5)

    stack.push(5, 0)
    assert stack.min_(0) == 5

    stack.push(10, 0)
    assert stack.min_(0) == 5

    stack.push(3, 0)
    assert stack.min_(0) == 3

    stack.pop(0)
    assert stack.min_(0) == 5
