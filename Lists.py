# For typing annotations
class Node:
    pass

class Node:
    def __init__(self, data, next_node: Node = None) -> None:
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

class LinkedList:
    class LinkedListIsEmpty(Exception):
        pass

    def __init__(self) -> None:
        # Init start_node
        self.start_node = None
        # self.setStartNode(None)

    def append(self, element):
        if self.isEmpty():
            self.setStartNode(Node(element))
        else:
            node = self.start_node
            while True:
                if node.getNextNode() is None:
                    node.setNextNode(Node(element))
                    break
                else:
                    node = node.getNextNode()

    def remove(self, element, return_value=False) -> Node | None:
        # Check is LinkedList has no nodes
        rv = None
        if self.isEmpty():
            raise LinkedList.LinkedListIsEmpty
        
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

    def insert(self, position, node: Node):
        node_to_insert = node

        if self.isEmpty():
            raise LinkedList.LinkedListIsEmpty
        
        node = self.start_node
        while True:

            if node is None:
                break
            if node.getData() == position:
                next_node = node.getNextNode()
                node_to_insert.setNextNode(next_node)
                node.setNextNode(node_to_insert)
                break
            node = node.getNextNode()
            
    def find(self, element) -> Node | None:
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

    def findPosition(self, element) -> int | None:
        if self.isEmpty():
            raise LinkedList.LinkedListIsEmpty
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

        return " -> ".join(s)