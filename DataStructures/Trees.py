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