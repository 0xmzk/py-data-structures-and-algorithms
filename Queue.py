class Queue:
    class QueueIsFull(Exception):
        pass

    class QueueIsEmpty(Exception):
        pass

    def __init__(self, size) -> None:
        self.size = size
        self.queue = [None] * size
        self.capacity = 0
        self.head_pointer = -1
        self.tail_pointer = 0

    def enqueue(self, element):
        if self._isFull():
            raise Queue.QueueIsFull
        else:
            if (self.head_pointer + 1) == self.size:
                idx = (self.head_pointer + 1) % self.size
            else:
                idx = self.head_pointer + 1
            self.queue[idx] = element
            self.head_pointer = idx
            self.capacity += 1

    def dequeue(self, return_value=False):
        if self._isEmpty():
            raise Queue.QueueIsEmpty
        else:
            self.capacity -= 1

            t = self.queue[self.tail_pointer]
            self.queue[self.tail_pointer] = None
            if (self.tail_pointer + 1) == self.size:
                idx = (self.tail_pointer + 1) % self.size
            else:
                idx = self.tail_pointer + 1
            self.tail_pointer = idx
            if return_value:
                return t


    def _isFull(self):
        if self.capacity == self.size:
            return True
        else:
            return False

    def _isEmpty(self):
        if self.capacity == 0:
            return True
        else:
            return False

    def printPointers(self):
        print(f"Head: {self.head_pointer}\nTail:{self.tail_pointer}")

    def __str__(self) -> str:
        return f"{self.queue}"

class DynamicQueue(Queue):
    def __init__(self, size) -> None:
        super().__init__(size)
        
    def _isFull(self):
        # C-like approach to expanding stack size
        if self.capacity == self.size:
            self.size += 1
            self.queue += [None]
            return False