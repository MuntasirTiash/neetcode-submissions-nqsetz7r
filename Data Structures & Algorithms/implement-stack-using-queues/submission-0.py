class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class MyStack:

    def __init__(self):
        self.left = Node(-1)
        self.right = Node(-1)
        self.left.next = self.right
        self.right.prev = self.left

    def push(self, x: int) -> None:
        new_node = Node(x)

        prev_node = self.right.prev
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = self.right
        self.right.prev = new_node
         

    def pop(self) -> int:
        target_node = self.right.prev
        value = target_node.value

        prev_node = target_node.prev
        prev_node.next = self.right
        self.right.prev = prev_node


        return value
        

    def top(self) -> int:
        target_node = self.right.prev
        value = target_node.value
        
        return value
        

    def empty(self) -> bool:
        return self.left.next == self.right


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()