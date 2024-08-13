

class QueueUsingList:
    def __init__(self):
        self.queue = []

    def enqueue(self, value: any) -> None:
        self.queue.append(value)

    def dequeue(self) -> any:
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def peek(self) -> any:
        if self.is_empty():
            return None
        return self.queue[0]

    def is_empty(self) -> bool:
        return len(self.queue) == 0

    def get_size(self) -> int:
        return len(self.queue)

    def print_queue(self) -> None:
        for item in self.queue:
            print(item, end=" -> ")
        print("None")
