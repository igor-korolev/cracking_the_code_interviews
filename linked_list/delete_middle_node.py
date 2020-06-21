# Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
# the first and last node, not necessarily the exact middle) of a singly linked list, given only
# access to that node. EXAMPLE input:the node c from the linked list a->b->c->d->e->f Result:
# nothing is returned, but the new linked list looks like a->b->d->e->f


from collections import namedtuple

import pytest

from linked_list.linked_list import Node, LinkedList


def delete_middle_node(node):
    if node is None or node.next_node is None:
        print(f"Warning: node '{node}' cannot be first or last one.")
        return False
    next_ = node.next_node
    node.data = next_.data
    node.next_node = next_.next_node
    return True


# Testing:
LListData = namedtuple("LListData", ["begin_nodes", "middle", "end_nodes", "expected"])


@pytest.fixture(
    scope="module",
    params=[
        LListData("ab", "c", "de", "abde"),
        LListData("ab", "c", "", "abc"),
    ],
    ids=lambda l: f"Input: {l.begin_nodes}-{l.middle}, Expected: {l.expected}",
)
def data_for_test(request):
    return request.param


def test_delete_middle_node(data_for_test):
    llist = LinkedList()
    llist.generate_nodes(data_for_test.begin_nodes)
    middle_node = Node(data_for_test.middle)
    llist.add_to_end(middle_node)
    llist.generate_nodes(data_for_test.end_nodes)
    delete_middle_node(middle_node)
    result = "".join(l.data for l in llist)
    assert result == data_for_test.expected, (
        f"Linked list: {data_for_test.begin_nodes}, remove node: {data_for_test.middle}' as input"
        f" produced '{result}', but '{data_for_test.expected}' expected"
    )
