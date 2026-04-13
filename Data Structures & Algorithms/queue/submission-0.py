class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.left = Node(-1)
        self.right = Node(-1)
        self.left.next = self.right
        self.right.prev = self.left


    def isEmpty(self) -> bool:
        return self.left.next == self.right
        

    def append(self, value: int) -> None:
        last_node = self.right.prev
        new_node = Node(value)

        last_node.next = new_node
        new_node.prev = last_node
        new_node.next = self.right
        self.right.prev = new_node

        

    def appendleft(self, value: int) -> None:
        first_node = self.left.next
        new_node = Node(value)

        new_node.next = first_node
        first_node.prev = new_node
        self.left.next = new_node
        new_node.prev = self.left
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1

        target_node = self.right.prev
        value = target_node.value

        prev_node = target_node.prev
        prev_node.next = self.right
        self.right.prev = prev_node

        return value
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        target_node = self.left.next
        value = target_node.value

        next_node = target_node.next

        self.left.next = next_node
        next_node.prev = self.left

        return value
        
