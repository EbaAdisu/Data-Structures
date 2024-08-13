from list_node import ListNode


class QueueUsingLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, value: any) -> None:
        new_node = ListNode(value)
        if self.rear is None:  # If queue is empty
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self) -> any:
        if self.front is None:  # If queue is empty
            return None
        value = self.front.val
        self.front = self.front.next
        if self.front is None:  # If the queue becomes empty after dequeue
            self.rear = None
        self.size -= 1
        return value

    def peek(self) -> any:
        if self.front is None:
            return None
        return self.front.val

    def is_empty(self) -> bool:
        return self.front is None

    def get_size(self) -> int:
        return self.size

    def print_queue(self) -> None:
        current_node = self.front
        while current_node:
            print(current_node.val, end=" -> ")
            current_node = current_node.next
        print("None")
