# Palindrome: Implement a function to check if a linked list is a palindrome.
# Palindrome is a word, phrase, or sequence that reads the same backward as forward
from collections import deque, namedtuple

import pytest

from linked_list.ln_list import LinkedList


def is_palindrome_reverse(llist):
    """
    This implementation is straight forward - make reverse linked list and compare it with
    original one.

    :param llist: Linked list.

    :returns: True if provided linked list is palindrome, False otherwise.
    """
    to_list = [n.data for n in llist]
    return to_list == to_list[::-1]


def is_palindrome_fast_slow(llist):
    """
    Check if the front half of the list is the reverse of the second half. To prepare a reverse
    part we use slow and fast runners - at each step in the loop, we push the data from the slow
    runner onto a stack. When the fast runner hits the end of the list, the slow runner will have
    reached the middle of the linked list. By this point, the stack will have all the elements
    from the front of the linked list, but in reverse order.

    :param llist: Linked list.

    :returns: True if provided linked list is palindrome, False otherwise.
    """
    fast = slow = llist.head
    first_half = []

    while fast is not None and fast.next_node is not None:
        first_half.append(slow.data)
        slow = slow.next_node
        fast = fast.next_node.next_node

    if fast is not None:  # This check is needed for odd-length linked lists
        slow = slow.next_node

    # Now slow is in the middle of linked list and we can compare to the first half stack
    while slow is not None:
        if first_half.pop() != slow.data:
            return False
        slow = slow.next_node
    return True


def is_palindrome_recursive(llist):
    """
    Recursive implementation. Using deque we pop elements out from the front and end of linked list.
    Then compare if these elements equal. The base case is when the length of the remained deque is
    less or equal 1.

    :param llist: Linked list.

    :returns: True if provided linked list is palindrome, False otherwise.
    """
    deq = deque([n.data for n in llist])

    def recurse(deq):
        if len(deq) > 1:
            first, last = deq.popleft(), deq.pop()
            if first != last:
                return False
            recurse(deq)
        return True

    return recurse(deq)


# Testing:
Llist = namedtuple("Llist", ["value", "expected"])


@pytest.fixture(
    scope="module",
    params=[
        Llist("asdfdsa", True),
        Llist("1234554321", True),
        Llist("a", True),
        Llist("12345", False),
        Llist("1232", False),
    ],
    ids=lambda ll: f"Input: {ll.value}, Expected: {ll.expected}",
)
def llist(request):
    return request.param


@pytest.mark.parametrize(
    "func", [is_palindrome_reverse, is_palindrome_fast_slow, is_palindrome_recursive]
)
def test_is_palindrome(func, llist):
    ll = LinkedList()
    ll.generate_nodes(llist.value)
    result = func(ll)
    assert result is llist.expected, (
        f"{func.__name__} with '{llist.value}' as input returned {result}, "
        f"but {llist.expected} expected"
    )
