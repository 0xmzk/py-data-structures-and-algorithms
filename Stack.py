class Stack:
    class StackIsEmpty(Exception):
        """Stack is empty"""
        pass


    class StackIsFull(Exception):
        """Stack is full"""
        pass

    def __init__(self, size) -> None:

        self.size = size
        self.top_pointer = -1
        self.stack = [None] * size

    def push(self, element):
        if self._isFull():
            raise Stack.StackIsFull
        else:
            self.stack[self.top_pointer + 1] = element
            self.top_pointer += 1

    def pop(self):
        if not self._isEmpty():
            rv = self.stack[self.top_pointer]
            self.stack[self.top_pointer] = None
            return rv
        else:
            raise Stack.StackIsEmpty

    def peek(self):
        if not self._isEmpty:
            return self.stack[self.top_pointer]
        else:
            raise Stack.StackIsEmpty

    def _isEmpty(self):
        if self.top_pointer == -1:
            return True
        else:
            return False

    def _isFull(self):
        if self.top_pointer == (self.size - 1):
            return True
        else:
            return False

    def __str__(self) -> str:
        return f"{self.stack}"


class DynamicStack(Stack):
    def __init__(self, size) -> None:
        super().__init__(size)

    def _isFull(self):
        if self.top_pointer == (self.size - 1):
            # C-like approach to expanding stack size
            self.size = self.size * 2
            temp = [None] * self.size
            for n,i in enumerate(self.stack):
                temp[n] = i
            self.stack = temp
            
            return False
        else:
            return False