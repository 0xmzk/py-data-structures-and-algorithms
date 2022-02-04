from Stack import Stack, DynamicStack
from Queue import Queue, DynamicQueue

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


# Stack_testing()
# Stack_testing(useDynamicStack=True)
# Queue_testing()
Queue_testing(useDynamicQueue=True)
