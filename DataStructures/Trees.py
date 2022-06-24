class BinaryNode:
    class RequiresLabel:
        def __str__(self) -> None:
            return "Node requires a label"

    def __init__(self, label: str) -> None:
        if not label:
            raise BinaryNode.RequiresLabel
        self.__label = label
        self.__left_node = None
        self.__right_node = None
        
        
    def setLeftNode(self, node):
        self.__left_node = node

    def getLeftNode(self):
        return self.__left_node

    def setRightNode(self, node):
        self.__right_node = node

    def getRightNode(self):
        return self.__right_node
    