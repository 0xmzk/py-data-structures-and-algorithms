from DataStructures.Queue import Queue, DynamicQueue

def test(useDynamicQueue=False):
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
