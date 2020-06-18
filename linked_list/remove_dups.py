# Remove Dups: Write code to remove duplicates from an unsorted linked list. FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?

from linked_list.linked_list import LinkedList

import pytest


def remove_dups(llist):
    """
    Remove duplicate nodes from a given linked list. Uses set to hold seen nodes. O(n).

    :param llist: Linked list object.
    :return: Linked list without duplicates.
    """
    current_node = llist.head
    if current_node is None:
        return llist

    seen_nodes = {current_node.data}

    while current_node.next_node is not None:
        if current_node.next_node.data in seen_nodes:
            current_node.next_node = current_node.next_node.next_node
        else:
            seen_nodes.add(current_node.next_node.data)
            current_node = current_node.next_node
    return llist


def remove_dups_without_extra_space(llist):
    """
    Remove duplicate nodes from a given linked list. It runs in O(n^2), but without extra buffer.

    :param llist: Linked list object.
    :return: Linked list without duplicates.
    """
    current = llist.head

    for node in llist:
        next_ = current.next_node
        while next_ is not None:
            if next_.data == node.data:
                next_ = next_.next_node
            else:
                next_ = next_.next_node
    return llist


# Testing:


@pytest.fixture(
    scope="module",
    params=[("abcad", "abcd"), ("", ""), ("aaa", "a"), ("aabbccd", "abcd")],
    ids=lambda l: f"Input: {l[0]}, Expected: {l[1]}",
)
def llist_data(request):
    ll_data, expected = request.param
    ll = LinkedList()
    ll.generate_nodes(ll_data)
    return ll, expected


@pytest.mark.parametrize("func", [remove_dups, remove_dups_without_extra_space])
def test_func_name(func, llist_data):
    ll, expected = llist_data
    result = "".join(n.data for n in func(ll))
    assert result == expected, (
        f"{func.__name__} with '{ll}' as input returned {result}, " f"but {expected} expected"
    )
