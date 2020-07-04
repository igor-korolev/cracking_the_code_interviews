from linked_list.ln_list import Node, DoublyLinkedList

import pytest


@pytest.fixture
def doubly_llist():
    llist = DoublyLinkedList()
    llist.generate_nodes("abc")
    return llist


def test_add_to_end(doubly_llist):
    last_node_in_orig_list = list(doubly_llist).pop()
    added_to_end = Node("e")
    doubly_llist.add_to_end(added_to_end)
    last_node = list(doubly_llist).pop()
    assert last_node == added_to_end, f"Last node must be {added_to_end}"
    assert last_node.next_node is None, "Next to appended node has to be None"
    assert (
        last_node_in_orig_list.next_node == added_to_end
    ), "Previous to the last node must be linked to newly added"
    assert (
        last_node.prev_node == last_node_in_orig_list
    ), f"Previous node of newly added should point to {last_node_in_orig_list}"


def test_add_to_beginning(doubly_llist):
    first_node_in_orig_list = doubly_llist.head
    insert_node = Node("first")
    doubly_llist.add_to_beginning(insert_node)
    assert doubly_llist.head == insert_node, f"First node must be {insert_node}"
    assert (
        doubly_llist.head.next_node == first_node_in_orig_list
    ), f"Next to inserted node hast to be previous head {first_node_in_orig_list}"
    assert (
        first_node_in_orig_list.prev_node == doubly_llist.head
    ), "Newly inserted node has to become the previous one to the second node"


def test_remove_node(doubly_llist):
    doubly_llist.remove_node("b")
    assert (
        doubly_llist.head.next_node.data == "c"
    ), "After deleting node 'b' next to the head must be node 'c'"
    assert [n.data for n in doubly_llist] == list("ac"), "Expected nodes: 'a, c'"
    node_c = doubly_llist.head.next_node
    assert (
        node_c.prev_node.data == "a"
    ), "After deleting node 'b', previous node of 'c'-node must be 'a'"


def test_add_to_end_when_head_is_none():
    llist = DoublyLinkedList()
    appended_node = Node("a")
    llist.add_to_end(appended_node)
    assert llist.head == appended_node, (
        f"After appending node {appended_node} to empty list its head must change to "
        f"{appended_node}"
    )
    assert llist.head.next_node is None, "Next node of head now should be None"
    assert llist.head.prev_node is None, "Previous node of head now should be None"


def test_add_to_beginning_when_head_is_none():
    llist = DoublyLinkedList()
    inserted_node = Node("a")
    llist.add_to_beginning(inserted_node)
    assert llist.head == inserted_node, (
        f"After inserting node {inserted_node} to empty list its head must change to "
        f"{inserted_node}"
    )
    assert llist.head.next_node is None, "Next node of head now should be None"
    assert llist.head.prev_node is None, "Previous node of head now should be None"


def test_remove_head(doubly_llist):
    head_before_deleting = doubly_llist.head
    new_head = head_before_deleting.next_node
    doubly_llist.remove_node(head_before_deleting.data)
    assert (
        doubly_llist.head == new_head
    ), f"After removing head {head_before_deleting} new head {new_head} expected"
    assert (
        doubly_llist.head.next_node.data == "c"
    ), "After deleting 'a', next node of head shoul be 'c'"
    assert doubly_llist.head.next_node.prev_node.data == "b"
    assert doubly_llist.head.prev_node is None


def test_raises_when_remove_unknown_node(doubly_llist):
    with pytest.raises(ValueError) as err:
        doubly_llist.remove_node("unknown-node")
        assert "'unknown-node' not found" in str(err), "Exception is expected about node not "


def test_raises_when_remove_from_empty_list():
    with pytest.raises(ValueError) as err:
        DoublyLinkedList().remove_node("some-node")
        assert "List is empty!" in str(err), "Exception is expected about empty list"
