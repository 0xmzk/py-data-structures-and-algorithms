from Stack import Stack, DynamicStack
from Queue import Queue, DynamicQueue
from Lists import LinkedList, Node
from Graphs import *

def Stack_testing(useDynamicStack=False):
    size = int(input("Enter Stack size:"))
    if useDynamicStack:
        myStack = DynamicStack(size)
    else:
        myStack = Stack(size)
    while True:
        print("Operations:")
        print("1: Print Stack")
        print("2: Push Element")
        print("3: Pop Element")
        print("4: Peek element")
        print("0: Exit")
        choice = int(input("Enter choice:"))
        if choice == 1:
            print(myStack)
        elif choice == 2:
            element = input("Enter element to push:")
            try:
                myStack.push(element)
            except Stack.StackIsFull:
                print("Stack is full cannot push element")
        elif choice == 3:
            try:
                pv = myStack.pop()
                print(f"Popped element: {pv}")
            except Stack.StackIsEmpty:
                print("Stack is empty cannot pop element")

        elif choice == 4:
            try:
                pv = myStack.peek()
                print(f"Peeked element: {pv}")
            except Stack.StackIsEmpty:
                print("Stack is empty cannot pop element")
            
        elif choice == 0:
            break

        
def Queue_testing(useDynamicQueue=False):
    size = int(input("Enter Queue size:"))
    if useDynamicQueue:
        myQueue = DynamicQueue(size)
    else:
        myQueue = Queue(size)
    while True:
        print("Operations:")
        print("1: Print Queue")
        print("2: Enqueue Element")
        print("3: Dequeue Element")
        print("0: Exit")
        choice = int(input("Enter choice:"))
        if choice == 1:
            print(myQueue)
        elif choice == 2:
            element = input("Enter element to enqueue:")
            try:
                myQueue.enqueue(element)
            except Queue.QueueIsFull:
                print("Queue is full cannot enqueue element")
        elif choice == 3:
            try:
                pv = myQueue.dequeue(return_value=True)
                print(f"Dequeued element: {pv}")
            except Queue.QueueIsEmpty:
                print("Queue is empty cannot dequeue element")
            
        elif choice == 0:
            break


def LinkedList_testing():
    myLinkedList = LinkedList()
    myLinkedList.append("A")
    myLinkedList.append("B")
    myLinkedList.append("C")
    myLinkedList.append("D")
    myLinkedList.append("E")

    print(myLinkedList)

    myLinkedList.remove("C")

    print(myLinkedList)

    myLinkedList.insert("B", Vertex("0"))

    print(myLinkedList)

    print(myLinkedList.findPosition("E"))
    print(myLinkedList.findPosition("x"))

def Graph_tests():
    A,B,C,D = [Vertex(i) for i in ["A","B","C","D"]]
    e1 = UndirectedEdge(A,B)
    e2 = UndirectedEdge(B,C)
    e3 = UndirectedEdge(C,D)
    e4 = UndirectedEdge(A,C)
    e5 = UndirectedEdge(B,D)
    v = {A,B,C,D}
    e = {e1,e2,e3,e4,e5}
    G = UndirectedGraph(v, e)
    # for vertex in v:
    #     print(f"{vertex}:{G.getVertexDegree(vertex)}")

# Stack_testing()
# Stack_testing(useDynamicStack=True)
# Queue_testing()
# Queue_testing(useDynamicQueue=True)
# LinkedList_testing()

Graph_tests()
