from list_node import ListNode


class StackUsingLinkedList:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value: any) -> None:
        new_node = ListNode(value)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self) -> any:
        if self.is_empty():
            return None
        value = self.top.val
        self.top = self.top.next
        self.size -= 1
        return value

    def peek(self) -> any:
        if self.is_empty():
            return None
        return self.top.val

    def is_empty(self) -> bool:
        return self.top is None

    def get_size(self) -> int:
        return self.size

    def print_stack(self) -> None:
        current_node = self.top
        while current_node:
            print(current_node.val, end=" -> ")
            current_node = current_node.next
        print("None")
