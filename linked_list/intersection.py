# Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the
# intersecting node. Note that the intersection is defined based on reference, not value.That
# is, if the kth node of the first linked list is the exact same node (by reference) as the jth
# node of the second linked list, then they are intersecting.

from collections import namedtuple

import pytest

from linked_list.ln_list import LinkedList


def get_intersection_node(ll1, ll2):
    """
    Algorithm: compute tails and lengths of two provided linked lists. If their tails aren't the
    same node, then no intersection. Otherwise we cut off the difference of lengths from the
    longer linked list and check nodes linearly.

    :param ll1: First linked list.
    :param ll2: Second linked list.
    :return: Node where linked lists are intersected or None.
    """
    ll1_tail, ll1_len = _tail_and_size(ll1)
    ll2_tail, ll2_len = _tail_and_size(ll2)

    if ll1_tail is not ll2_tail:  # If tails aren't equal - there is no intersection
        return None

    shorter, longer = (ll1, ll2) if ll1_len < ll2_len else (ll2, ll1)
    size_diff = abs(ll1_len - ll2_len)
    longer_pointer = longer.head
    while size_diff:
        longer_pointer = longer_pointer.next_node  # Chop off from the beginning of longer list
        size_diff -= 1

    shorter_pointer = shorter.head

    while shorter_pointer is not None:  # Finding intersection node
        if shorter_pointer is longer_pointer:
            return shorter_pointer
        shorter_pointer, longer_pointer = shorter_pointer.next_node, longer_pointer.next_node


def _tail_and_size(ll):
    """
    Helper func to obtain tail and size of linked list.

    :param ll: Linked list.
    :return: Tuple of two - (tail node, linked list length).
    """
    ll_tail = ll.head
    ll_len = 0
    while ll_tail is not None:
        ll_tail = ll_tail.next_node
        ll_len += 1
    return (ll_tail, ll_len)


# Testing:
Llists = namedtuple("Llists", ["ll1", "ll2", "expected"])


def _prepare_llists_for_test():
    """Prepare test data."""
    ll1, ll2 = LinkedList(), LinkedList()
    ll1.generate_nodes("defg")
    ll2.generate_nodes("abc")

    ll2.head.next_node.next_node = ll1.head  # intersect lists in the middle
    positive = [(ll1, ll2, ll1.head), (ll1, ll1, ll1.head)]

    neg_ll = LinkedList()
    neg_ll.generate_nodes("abc")
    negative = [(ll1, neg_ll, None), (ll2, neg_ll, None)]
    return positive + negative


@pytest.fixture(
    scope="module",
    params=_prepare_llists_for_test(),
    ids=lambda ll: f"Input: {ll[0]} and {ll[1]}, Expected: {ll[2]}",
)
def llists(request):
    return Llists(*request.param)


def test_get_intersection_node(llists):
    result = get_intersection_node(llists.ll1, llists.ll2)
    assert result is llists.expected, (
        f"{get_intersection_node} with '{llists.ll1}' and '{llists.ll2}' as input returned"
        f" {result}, but {llists.expected} expected"
    )
