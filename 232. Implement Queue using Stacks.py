class MyQueue:

    def __init__(self):
        self.stack = []
        self.front = 0

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        self.front += 1
        return self.stack[self.front - 1]

    def peek(self) -> int:
        return self.stack[self.front]

    def empty(self) -> bool:
        return self.front == len(self.stack)