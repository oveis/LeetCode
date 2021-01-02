class Node:
    def __init__(self, key: int, value: int, pre_node=None, next_node=None):
        self.key = key
        self.val = value
        self.pre_node = pre_node
        self.next_node = next_node
        

class LRUCache:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cur_size = 0
        self.key_to_node = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0, self.head)
        self.head.next_node = self.tail
        

    def get(self, key: int) -> int:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            self.delete_node(node)
            self.add_node(node)
            return node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key not in self.key_to_node:
            node = Node(key, value)
            self.key_to_node[key] = node
            self.add_node(node)
            self.cur_size += 1
            
            if self.cur_size > self.capacity:
                node = self.head.next_node
                del self.key_to_node[node.key]
                self.delete_node(node)
                self.cur_size -= 1
        else:
            node = self.key_to_node[key]
            node.val = value
            self.delete_node(node)
            self.add_node(node)
            
                
    def delete_node(self, node):
        node.pre_node.next_node = node.next_node
        if node.next_node:
            node.next_node.pre_node = node.pre_node
        else:
            self.tail = node.pre_node
        
        
    def add_node(self, node):
        self.tail.pre_node.next_node = node
        node.pre_node = self.tail.pre_node
        node.next_node = self.tail
        self.tail.pre_node = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
