"""Linked list(singly and doubly) implemented in python."""


class Node:
    """Represents nodes of the linked lists."""

    def __init__(self, data, next_node=None, prev_node=None):
        """
        :param data: Value of node.
        :param next_node: Link to the next node.
        :param prev_node: Link to the previous node.
        """
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

    def __repr__(self):
        return str(self.data)


class LinkedList:
    """Singly linked list."""

    def __init__(self):
        self.head = None

    def generate_nodes(self, nodes_data):
        """
        Prepares nodes - can be used for quick testing.

        :param nodes_data: Any iterable.
        """
        for elem in nodes_data:
            self.add_to_end(Node(elem))

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next_node
        nodes.append("None")
        return " -> ".join(str(n) for n in nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next_node

    def __len__(self):
        ll_len = 0
        node = self.head
        while node is not None:
            ll_len += 1
            node = node.next_node
        return ll_len

    def add_to_end(self, node):
        """
        Appends node to the end of a linked list.

        :param Node node: Node to append.
        """
        if self.head is None:
            self.head = node
        else:
            list(self).pop().next_node = node

    def add_to_beginning(self, node):
        """
        Insert node to the beginning of a linked list.

        :param Node node: Node to insert.
        """
        if self.head is None:
            self.head = node
        else:
            self.head, node.next_node = node, self.head

    def _find_nodes(self, node_data):
        """
        Helper method to find the node by provided data and corresponing previous node.

        :param node_data: Value of the node to find.
        :return: Tuple of two - (found node, previous node).
        :raises ValueError: In case of empty list or if node not found.
        """
        previous_node = self.head
        for node in self:
            if node.data == node_data:
                previous_node.next_node = node.next_node
                return node, previous_node
            previous_node = node
        else:
            raise ValueError(f"Node with data '{node_data}' not found!")

    def remove_node(self, node_data):
        """
        Deletes node from a linked list by provided data.

        :param node_data: Value of the node to find.
        """
        if self.head is None:
            raise ValueError("List is empty!")

        if self.head.data == node_data:
            self.head = self.head.next_node
        else:
            node_to_remove, previous_node = self._find_nodes(node_data)
            previous_node.next_node = node_to_remove.next_node


class DoublyLinkedList(LinkedList):
    """
    Doubly linked list. Nodes in such lists have connections in both directions(next and previous).
    """

    def __repr__(self):
        return super().__repr__().replace("->", "<-->")

    def add_to_end(self, node):
        """
        Appends node to the end of a linked list.

        :param Node node: Node to append.
        """
        if self.head is None:
            self.head = node
        else:
            last = list(self).pop()
            last.next_node = node
            node.prev_node = last

    def add_to_beginning(self, node):
        """
        Insert node to the beginning of a linked list.

        :param Node node: Node to insert.
        """
        if self.head is None:
            self.head = node
        else:
            self.head.prev_node = node
            self.head, node.next_node = node, self.head

    def remove_node(self, node_data):
        """
        Deletes node from a linked list by provided data.

        :param node_data: Value of the node to find.
        """
        if self.head is None:
            raise ValueError("List is empty!")

        if self.head.data == node_data:
            self.head = self.head.next_node
            self.head.prev_node = None
        else:
            node_to_remove, previous_node = self._find_nodes(node_data)
            previous_node.next_node = node_to_remove.next_node
            node_to_remove.next_node.prev_node = previous_node
