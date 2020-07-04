from linked_list.ln_list import Node, LinkedList

import pytest


@pytest.fixture
def singly_llist():
    llist = LinkedList()
    llist.generate_nodes("abc")
    return llist


def test_add_to_end(singly_llist):
    last_node_in_orig_list = list(singly_llist).pop()
    added_to_end = Node("e")
    singly_llist.add_to_end(added_to_end)
    last_node = list(singly_llist).pop()
    assert last_node == added_to_end, f"Last node must be {added_to_end}"
    assert last_node.next_node is None, "Next to appended node has to be None"
    assert (
        last_node_in_orig_list.next_node == added_to_end
    ), "Previous to the last node must be linked to newly added"


def test_add_to_beginning(singly_llist):
    first_node_in_orig_list = singly_llist.head
    insert_node = Node("first")
    singly_llist.add_to_beginning(insert_node)
    assert singly_llist.head == insert_node, f"First node must be {insert_node}"
    assert (
        singly_llist.head.next_node == first_node_in_orig_list
    ), f"Next to inserted node hast to be previous head {first_node_in_orig_list}"


def test_remove_node(singly_llist):
    singly_llist.remove_node("b")
    assert (
        singly_llist.head.next_node.data == "c"
    ), "After deleting node 'b' next to the head must be node 'c'"
    assert [n.data for n in singly_llist] == list("ac"), "Expected nodes: 'a, c'"


def test_add_to_end_when_head_is_none():
    llist = LinkedList()
    appended_node = Node("a")
    llist.add_to_end(appended_node)
    assert llist.head == appended_node, (
        f"After appending node {appended_node} to empty list its head must change to "
        f"{appended_node}"
    )
    assert llist.head.next_node is None, "Next node of head now should be None"


def test_add_to_beginning_when_head_is_none():
    llist = LinkedList()
    inserted_node = Node("a")
    llist.add_to_beginning(inserted_node)
    assert llist.head == inserted_node, (
        f"After inserting node {inserted_node} to empty list its head must change to "
        f"{inserted_node}"
    )
    assert llist.head.next_node is None, "Next node of head now should be None"


def test_remove_head(singly_llist):
    head_before_deleting = singly_llist.head
    new_head = head_before_deleting.next_node
    singly_llist.remove_node(head_before_deleting.data)
    assert (
        singly_llist.head == new_head
    ), f"After removing head {head_before_deleting} new head {new_head} expected"
    assert (
        singly_llist.head.next_node.data == "c"
    ), "After deleting 'a', next node of head should be 'c'"


def test_raises_when_remove_unknown_node(singly_llist):
    with pytest.raises(ValueError) as err:
        singly_llist.remove_node("unknown-node")
        assert "'unknown-node' not found" in str(err), "Exception is expected about node not "


def test_raises_when_remove_from_empty_list():
    with pytest.raises(ValueError) as err:
        LinkedList().remove_node("some-node")
        assert "List is empty!" in str(err), "Exception is expected about empty list"
