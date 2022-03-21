from DataStructures.Lists import LinkedList


def test(double_linked=False):
    myLinkedList = LinkedList(double_linked=double_linked)
    myLinkedList.append("A")
    myLinkedList.append("B")
    myLinkedList.append("C")
    myLinkedList.append("D")
    myLinkedList.append("E")

    print(myLinkedList)

    myLinkedList.remove("C")

    print(myLinkedList)

    myLinkedList.insert("B", "1")

    print(myLinkedList)

    print(myLinkedList.findPosition("E"))
    print(myLinkedList.findPosition("x"))
    print(myLinkedList.getElement("1").getPreviousNode())
