# For typing annotations
from abc import ABC

class AbstractNode(ABC):
    pass

class Node(AbstractNode):
    class NotDuallyLinked(Exception):
        def __str__(self):
            return "Node is not dually linked - set 'double_linked' bool to True to use this functionality "

    def __init__(self, data, next_node: AbstractNode = None) -> None:
        self.next_node = next_node
        self.data = data

    def getNextNode(self):
        return self.next_node

    def getNextNodeData(self):
        return self.next_node.getData()

    def setNextNode(self, next_node):
        self.next_node = next_node

    def getData(self):
        return self.data

    def getPreviousNode(self):
        raise Node.NotDuallyLinked

    def getPreviousNodeData(self):
        raise Node.NotDuallyLinked

    def setPreviousNodeData(self):
        raise Node.NotDuallyLinked

    @staticmethod
    def insertNode(insert_position, node_to_insert):
        next_node = insert_position.getNextNode()
        node_to_insert.setNextNode(next_node)
        insert_position.setNextNode(node_to_insert)
    
    @staticmethod
    def appendNode(append_position, node_to_append):
        append_position.setNextNode(node_to_append)

class DuallyLinkedNode(Node):
    def __init__(self, data, next_node: Node = None, previous_node: Node = None) -> None:
        super().__init__(data, next_node)
        self.previous_node = previous_node

    def getPreviousNode(self):
        return self.previous_node

    def getPreviousNodeData(self):
        return self.previous_node.getData()

    def setPreviousNode(self, previous_node):
        self.previous_node = previous_node

    @staticmethod
    def insertNode(insert_position, node_to_insert):
        next_node = insert_position.getNextNode()
        next_node.setPreviousNode(node_to_insert)
        node_to_insert.setNextNode(next_node)
        node_to_insert.setPreviousNode(insert_position)
        insert_position.setNextNode(node_to_insert)

    @staticmethod
    def appendNode(append_position, node_to_append):
        node_to_append.setPreviousNode(append_position)
        append_position.setNextNode(node_to_append)

class LinkedList:
    class ListIsEmpty(Exception):
        pass

    def __init__(self, double_linked=False) -> None:
        if double_linked:
            self.Node = DuallyLinkedNode
        else:
            self.Node = Node

        # Init start_node
        self.setStartNode(None)

    def append(self, element:str):
        """Append given element to the end of the list"""
        if self.isEmpty():
            self.setStartNode(self.Node(element))
        else:
            node = self.start_node
            while True:
                if node.getNextNode() is None:
                    self.Node.appendNode(node, self.Node(element))
                    break
                else:
                    node = node.getNextNode()

    def remove(self, element:str, return_value=False) -> DuallyLinkedNode | Node | None:
        """Remove a given element from list"""
        # Check is LinkedList has no nodes
        rv = None
        if self.isEmpty():
            raise LinkedList.ListIsEmpty
        
        node = self.start_node
        # Special check case for start node
        # Check if start node is the element to delete
        if node.getData() == element:
            if return_value:
                rv = node
            self.setStartNode(node.getNextNode())
            return rv
        else:
            while True:
                if node is None:
                    break
                # For each node in the list,
                # check the the data of each next node before moving onto the next node
                if node.getNextNodeData() == element:
                    # If node is found, then remove it from chain by taking all other
                    # nodes that it points to and assigning them to previous node.
                    if return_value:
                        rv = node.getNextNode()
                    matched_nodes_next_nodes = node.getNextNode().getNextNode()
                    node.setNextNode(matched_nodes_next_nodes)
                    break
                node = node.getNextNode()
            return rv

    def insert(self, element: str, data: str):
        """Insert given data as the next node of given element"""
        node_to_insert = self.Node(data)

        # Check if list is empty
        if self.isEmpty():
            raise LinkedList.ListIsEmpty
        
        node = self.start_node
        # Begin iterating over list
        while True:
            if node is None:
                # If list element is not found, then no change is made
                # TODO: raise exception if no element is found
                break
            if node.getData() == element:
                self.Node.insertNode(node, node_to_insert)
                break
            node = node.getNextNode()

    def getElement(self, element: str) -> DuallyLinkedNode  | None:
        if self.isEmpty():
            raise LinkedList.LinkedListIsEmpty
        rv = None
        node = self.start_node
        while True:
            if node is None:
                break
            if node.getData() == element:
                rv = node
                break
            node = node.getNextNode()
        return rv

    def findPosition(self, element:str) -> int | None:
        if self.isEmpty():
            raise LinkedList.ListIsEmpty
        rv = -1
        node = self.start_node
        while True:
            rv += 1
            if node is None:
                rv = None
                break
            if node.getData() == element:
                break
            node = node.getNextNode()
        return rv
    
    def isEmpty(self):
        if self.start_node is None:
            return True
        else:
            return False

    def setStartNode(self, node):
        self.start_node = node       

    def __len__(self):
        if self.isEmpty():
            return 0
        length = 0
        node = self.start_node
        while True:
            if node is None:
                break
            else:
                length += 1
            node = node.getNextNode()
        return length
        
    def __str__(self) -> str:
        node = self.start_node
        s = []
        while True:
            if node is None:
                break
            else:
                s.append(node.getData())
                node = node.getNextNode()
        if self.Node == Node:
            return " -> ".join(s)
        elif self.Node == DuallyLinkedNode:
            return " <-> ".join(s)