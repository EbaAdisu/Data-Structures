class StackUsingList:
    def __init__(self):
        self.stack = []

    def push(self, value: any) -> None:
        self.stack.append(value)

    def pop(self) -> any:
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self) -> any:
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def get_size(self) -> int:
        return len(self.stack)

    def print_stack(self) -> None:
        for item in reversed(self.stack):
            print(item, end=" -> ")
        print("None")
