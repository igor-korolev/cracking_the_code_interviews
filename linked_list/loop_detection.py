# Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
# beginning of the loop.
# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node's next_node pointer points to an earlier
# node, so as to make a loop in the linked list.
# EXAMPLE
# Input: A -> B -> C -> D -> E -> C[the same C as earlier]
# Output: C

import pytest

from linked_list.ln_list import LinkedList


def detect_loop_node(ll):
    """
    Firstly, algorithm finds out that loop exists, than finds a loop node. Using fast/slow runner
    technique.

    :param ll: Linked list.
    :return: Node, where loop starts or None if there is no loops.
    """
    fast = slow = ll.head

    # To identify if loop exists we use slow/fast runners. Like racing cars with different speeds
    # will eventually collide (in circle)
    while fast is not None and fast.next_node is not None:
        fast = fast.next_node.next_node
        slow = slow.next_node

        if fast is slow:  # This is the indicator of loop
            break

    if fast is None or fast.next_node is None:
        return None

    # Now to identify the targeted node, where loop begins, we need to step with the same speed -
    # one runner will start from the beginning, the other from the node, where they collided
    slow = ll.head
    while fast is not slow:
        fast = fast.next_node
        slow = slow.next_node

    return fast


@pytest.fixture
def looped_llist():
    ll = LinkedList()
    ll.generate_nodes("abcdefgh")

    loop_node = ll.head.next_node

    last = ll.head
    while last.next_node is not None:
        last = last.next_node

    last.next_node = loop_node  # Append to last node loop node
    return ll, loop_node


def test_get_loop_node_positive(looped_llist):
    ll, expected = looped_llist
    assert detect_loop_node(ll) == expected, "Found wrong node"


def test_get_loop_node_negative():
    ll = LinkedList()
    ll.generate_nodes("abc")  # No loop
    assert detect_loop_node(ll) is None, "None expected, because there's no loop in the linked list"
