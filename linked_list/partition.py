# Partition: Write code to partition a linked list around a value x, such that all nodes less
# than x come before all nodes greater than or equal to x. If x is contained within the list,
# the values of x only need to be after the elements less than x (see below). The partition
# element x can appear anywhere in the "right partition"; it does not need to appear between the
# left and right partitions.
# EXAMPLE # Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1[partition=5]
# Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
from collections import namedtuple

import pytest

from linked_list.ln_list import LinkedList, Node


def do_partition(llist, partition):
    """
    Partition linked list around provided pivot. This implementation collects all nodes that
    are less than a pivot, and builds new partitioned linked list.

    :param llist: Instance of `LinkedList`.
    :param partition: Value of pivot to partition linked lists' smaller values
    :return: Partitioned linked list.
    """
    if llist.head is None:
        print("Cannot find in empty list")
        return llist

    less = more = None
    current = llist.head
    last_less = None  # needed to remember the last Node of less before None

    while current is not None:
        remembered_next = current.next_node
        if current.data < partition:
            if less is None:
                less = Node(current.data)
                last_less = less
            else:
                less, less.next_node = current, less
        else:
            if more is None:
                more = Node(current.data)
            else:
                more, more.next_node = current, more
        current = remembered_next

    last_less.next_node = more

    partitioned = LinkedList()
    partitioned.head = less
    return partitioned


def do_partition2(llist, partition):
    """
    Partition linked list around provided pivot. This implementation makes in-place swaps

    :param llist: Instance of `LinkedList`.
    :param partition: Value of pivot to partition linked lists' smaller values
    :return: Partitioned linked list.
    """
    if llist.head is None:
        print("Cannot find in empty list")
        return llist

    current = llist.head.next_node
    prev = llist.head

    while current is not None:
        next_ = current.next_node  # remember next, because current can be moved to the beginning
        if current.data < partition:
            prev.next_node = next_
            current.next_node = llist.head
            llist.head = current
        else:
            prev = current  # need to update previous only if swapping wasn't done

        current = next_

    return llist


ll = LinkedList()
ll.generate_nodes([3, 5, 8, 5, 10, 2, 1])
do_partition2(ll, 5)

# Testing:

LlistData = namedtuple("LlistData", ["llist", "pivot"])


@pytest.fixture(
    scope="module",
    params=[
        LlistData([3, 5, 8, 5, 10, 2, 1], 5),
        LlistData([1, 8, 8, 3, 50, 5, 9], 8),
        LlistData([], 5),
        LlistData([3, 2], 3),
    ],
)
def llist_data(request):
    ll = LinkedList()
    ll.generate_nodes(request.param.llist)
    return ll, request.param.pivot


@pytest.mark.parametrize("func", [do_partition, do_partition2])
def test_partition(func, llist_data):
    ll, pivot = llist_data
    less_than_pivot_in_original = [node.data for node in ll if node.data < pivot]

    result = func(ll, pivot)

    less_than_pivot_after_partition = []
    for node in result:
        if node.data == pivot:
            break
        less_than_pivot_after_partition.append(node.data)

    assert all(
        n >= pivot
        for n in [
            i for i in less_than_pivot_after_partition if i not in set(less_than_pivot_in_original)
        ]
    )
