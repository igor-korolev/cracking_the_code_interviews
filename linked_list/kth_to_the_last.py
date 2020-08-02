# Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked
# list.

from collections import namedtuple

import pytest

from linked_list.ln_list import LinkedList


def get_kth_to_the_last(llist, k):
    """
    Finds kth to last element in linked list. Based on length.

    :param llist: Instance of LinkedList.
    :return: Value of the k-th to last node or None if linked list is empty.
    """
    if llist.head is None:
        return

    length = len(list(llist))
    node = llist.head
    for i in range(length - k):
        node = node.next_node
    return node.data


def get_kth_to_last2(llist, k):
    """
    Finds kth to last element in linked list. Uses two pointers.

    :param llist: Instance of LinkedList.
    :return: Value of the k-th to last node or None if linked list is empty.
    """
    if llist.head is None:
        return

    to_the_end_pointer = target_pointer = llist.head

    for i in range(k):  # iterate k times from the beginning
        to_the_end_pointer = to_the_end_pointer.next_node

    while to_the_end_pointer:  # when this pointer reaches the end of linked list
        target_pointer = target_pointer.next_node  # this one will be the kth elem from the end
        to_the_end_pointer = to_the_end_pointer.next_node

    return target_pointer.data


# Testing:


LList = namedtuple("LList", ["input_list", "k", "expected"])


@pytest.fixture(
    scope="module",
    params=[LList("abc", 2, "b"), LList("abc", 1, "c"), LList("abc", 3, "a"), LList("", 3, None)],
    ids=lambda l: f"Input: {l.input_list}-{l.k}, Expected: {l.expected}",
)
def llist(request):
    return request.param


@pytest.mark.parametrize("func", [get_kth_to_the_last, get_kth_to_last2])
def test_kth_to_the_last(func, llist):
    ll = LinkedList()
    ll.generate_nodes(llist.input_list)

    result = func(ll, llist.k)
    assert result == llist.expected, (
        f"{func.__name__} with '{llist.input_list}-{llist.k}' as input returned {result}, "
        f"but {llist.expected} expected"
    )
