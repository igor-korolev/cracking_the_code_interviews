# sum lists: you have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the
# list. Write a function that adds the two numbers and returns the sum as a linked list.
# EXAMPLE
# input:(7-> 1 -> 6) + (5 -> 9 -> 2). that is, 617 + 295. output: 2 -> 1 -> 9. that is, 912.
# Follow up suppose the digits are stored in forward order. Repeat the above problem.
# EXAMPLE
# input:(6 -> 1 -> 7) + (2 -> 9 -> 5).that is,617 + 295. output:9 -> 1 -> 2. that is, 912.

from collections import namedtuple

import pytest

from linked_list.ln_list import LinkedList, Node


def sum_lists(llist1, llist2):
    """
    Solution using type conversions.

    :param llist1: First linked list.
    :param llist2: Second linked list.
    :return: Reversed sum of linked lists' reversed numbers.
    """
    first_num = int("".join(str(n) for n in list(llist1)[::-1]))
    second_num = int("".join(str(n) for n in list(llist2)[::-1]))
    sum_ = [int(s) for s in list(str(first_num + second_num))[::-1]]
    sum_llist = LinkedList()
    sum_llist.generate_nodes(sum_)
    return sum_llist


def sum_lists2(llist1, llist2):
    """
    Algorithmic solution using divmod operation.

    :param llist1: First linked list.
    :param llist2: Second linked list.
    :return: Reversed sum of linked lists' reversed numbers.
    """
    head1, head2 = llist1.head, llist2.head
    result_ll = LinkedList()
    remainder = 0

    while head1 is not None or head2 is not None:
        result = remainder
        if head1 is not None:
            result += head1.data
            head1 = head1.next_node
        if head2 is not None:
            result += head2.data
            head2 = head2.next_node

        remainder, node_data = divmod(result, 10)
        result_ll.add_to_end(Node(node_data))

    if remainder:
        result_ll.add_to_end(Node(remainder))

    return result_ll


def sum_lists_followup(llist1, llist2):
    """
    Solution using type conversions.

    :param llist1: First linked list.
    :param llist2: Second linked list.
    :return: Reversed sum of linked lists' reversed numbers.
    """
    first_num = int("".join(str(n) for n in list(llist1)))
    second_num = int("".join(str(n) for n in list(llist2)))
    sum_ = [int(s) for s in list(str(first_num + second_num))]
    sum_llist = LinkedList()
    sum_llist.generate_nodes(sum_)
    return sum_llist


def sum_lists_followup2(llist1, llist2):
    """
    Algorithmic solution using base 10.

    :param llist1: First linked list.
    :param llist2: Second linked list.
    :return: Reversed sum of linked lists' reversed numbers.
    """
    len_l1, len_l2 = len(llist1), len(llist2)
    if len_l1 > len_l2:
        for i in range(len_l1 - len_l2):
            llist2.add_to_beginning(Node(0))
    else:
        for i in range(len_l2 - len_l1):
            llist1.add_to_beginning(Node(0))
    power = len(llist1) - 1  # take any of two as we equalized length by filling with zeros the shorter list
    head1, head2 = llist1.head, llist2.head

    sum_ = 0
    while head1 is not None and head2 is not None:
        sum_ = sum_ + head1.data * (10 ** power) + head2.data * (10 ** power)
        power -= 1
        head1, head2 = head1.next_node, head2.next_node

    result_ll = LinkedList()
    result_ll.generate_nodes(int(n) for n in str(sum_))
    return result_ll


# Testing:
Llists = namedtuple("Llists", ["ll1", "ll2", "expected"])


@pytest.fixture(
    scope="module",
    params=[
        Llists([7, 1, 6], [5, 9, 2], [2, 1, 9]),
        Llists([1, 1, 1], [2, 2, 2], [3, 3, 3]),
        Llists([1, 2], [3, 4, 5], [4, 6, 5]),
    ],
    ids=lambda s: f"Input: {s.ll1},{s.ll2}, Expected: {s.expected}",
)
def llists_data(request):
    ll1, ll2 = LinkedList(), LinkedList()
    ll1.generate_nodes(request.param.ll1)
    ll2.generate_nodes(request.param.ll2)
    return ll1, ll2, request.param.expected


@pytest.mark.parametrize("func", [sum_lists, sum_lists2])
def test_sum_lists(func, llists_data):
    ll1, ll2, expected = llists_data
    result = [n.data for n in func(ll1, ll2)]
    assert result == expected, (
        f"{func.__name__} with two linked lists: '{ll1}', '{ll2}' as input "
        f"returned {result}, but {expected} expected"
    )


@pytest.fixture(
    scope="module",
    params=[
        Llists([6, 1, 7], [2, 9, 5], [9, 1, 2]),
        Llists([1, 1, 1], [2, 2, 2], [3, 3, 3]),
        Llists([1, 2], [3, 4, 5], [3, 5, 7]),
    ],
    ids=lambda s: f"Input: {s.ll1},{s.ll2}, Expected: {s.expected}",
)
def followup_data(request):
    ll1, ll2 = LinkedList(), LinkedList()
    ll1.generate_nodes(request.param.ll1)
    ll2.generate_nodes(request.param.ll2)
    return ll1, ll2, request.param.expected


@pytest.mark.parametrize("func", [sum_lists_followup, sum_lists_followup2])
def test_sum_lists_followup(func, followup_data):
    ll1, ll2, expected = followup_data
    result = [n.data for n in func(ll1, ll2)]
    assert result == expected, (
        f"{func.__name__} with two linked lists: '{ll1}', '{ll2}' as input "
        f"returned {result}, but {expected} expected"
    )
