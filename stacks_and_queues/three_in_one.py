# Three in One: Describe how you could use a single array to implement three stacks.


class TripleStack:
    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.num_stacks = 3
        self.array = [None] * (self.stack_size * self.num_stacks)
        self.sizes = {stack: 0 for stack in range(self.num_stacks)}

    def push(self, item, stack_num):
        if self.sizes[stack_num] >= self.stack_size:
            raise ValueError(f"Stack {stack_num} is full")
        self.sizes[stack_num] = 1
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


def test_is_empty():
    stack = TripleStack(stack_size=2)

    assert stack.is_empty(1) is True
    stack.push("a", 1)
    assert stack.is_empty(1) is False


def test_peek_and_push():
    stack = TripleStack(stack_size=2)

    first_stack_val = "a"
    stack.push(first_stack_val, 0)
    assert stack.peek(0) == first_stack_val

    second_stack_val = "b"
    stack.push(second_stack_val, 1)
    assert stack.peek(1) == second_stack_val

    third_stack_val = "c"
    stack.push(third_stack_val, 2)
    assert stack.peek(2) == third_stack_val


def test_pop():
    stack = TripleStack(stack_size=2)

    val_to_push = "a"
    stack.push(val_to_push, 0)

    assert stack.pop(0) == val_to_push
