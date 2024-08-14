from list_node import ListNode


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_at_beginning(self, value: any) -> None:
        if self.head is None:
            self.head = ListNode(value)
            self.tail = self.head
        else:
            node = ListNode(value)
            node.next = self.head
            self.head = node
        self.size += 1

    def instert_at_end(self, value: any) -> None:
        if self.head is None:
            self.head = ListNode(value)
            self.tail = self.head
        else:
            node = ListNode(value)
            self.tail.next = node
            self.tail = node
        self.size += 1

    def insert_at_position(self, position: int, value: any) -> None:
        if position > self.size or position < 0:
            return
        elif position == 0:
            self.insert_at_beginning(value)
        elif position == self.size:
            self.instert_at_end(value)
        else:
            current_node = self.head
            for _ in range(position-1):
                current_node = current_node.next
            new_node = ListNode(value)
            new_node.next = current_node.next
            current_node.next = new_node

    def get_head(self) -> ListNode:
        if self.head:
            return self.head

    def get_tail(self) -> ListNode:
        if self.tail:
            return self.tail

    def get_at_position(self, position: int) -> ListNode:
        if not self.is_valid_position(position):
            return

        current_node = self.head
        for _ in range(position):
            current_node = current_node.next
        return current_node

    def update_at_position(self, position, value) -> None:
        if not self.is_valid_position(position):
            return

        current_node = self.head
        for _ in range(position):
            current_node = current_node.next
        current_node.val = value

    def delete_at_beginning(self) -> None:
        if self.head:
            self.head = self.head.next
            self.size -= 1
            if self.head is None:
                self.tail = None

    def delete_at_end(self) -> None:
        if self.head:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                current_node = self.head
                while current_node.next != self.tail:
                    current_node = current_node.next
                current_node.next = None
                self.tail = current_node
            self.size -= 1

    def delete_at_position(self, position) -> None:
        if not self.is_valid_position(position):
            return
        if position == 0:
            self.delete_at_beginning()
        elif position == self.size - 1:
            self.delete_at_end()
        else:
            current_node = self.head
            for _ in range(position - 1):
                current_node = current_node.next
            current_node.next = current_node.next.next
            self.size -= 1

    def find(self, value) -> ListNode:
        current_node = self.head
        while current_node:
            if current_node.val == value:
                return current_node
            current_node = current_node.next
        return None

    def size(self) -> int:
        return self.size

    def is_empty(self) -> bool:
        return self.size == 0

    def is_valid_position(self, position):
        return 0 <= position < self.size

    # Additional methods

    def reverse(self) -> None:
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head, self.tail = self.tail, self.head

    def print_list(self) -> None:
        current_node = self.head
        while current_node:
            print(current_node.val, end=" -> ")
            current_node = current_node.next
        print("None")

    def to_list(self) -> list:
        elements = []
        current_node = self.head
        while current_node:
            elements.append(current_node.val)
            current_node = current_node.next
        return elements

    def from_list(self, values) -> None:
        for value in values:
            self.insert_at_end(value)

    def has_cycle(self) -> bool:
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
