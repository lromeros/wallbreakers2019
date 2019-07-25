class LRUCacheNode:
    
     def __init__(self, key, val, parent=None, child=None):
        self.key = key
        self.val = val
        self.parent = parent
        self.child = child
        
class LRUCache:

    def __init__(self, capacity: int):
        self.head = None
        self.tail = None
        self.nums = 0
        self.capacity = capacity
        self.node_dict = {}
    
    def _delete_tail(self):
        self.node_dict.pop(self.tail.key)
        self.tail.parent.child = None
        new_tail = self.tail.parent
        self.tail.parent = None
        self.tail = new_tail
        
    def _move_node_to_front(self, node):
        # node exists in this list
        if self.head != node:
            node.parent.child = node.child
            if self.tail != node:
                node.child.parent = node.parent
            else:
                self.tail = node.parent
            self.head.parent = node
            node.parent = None
            node.child = self.head
            self.head = node
        
        
    def _add_node_to_front(self, node):
        if self.head == None and self.tail == None:
            self.head = node
            self.tail = node
        else:
            node.child = self.head
            self.head.parent = node
            self.head = node

    def get(self, key: int) -> int:
        node = self.node_dict.get(key, -1)
        if node != -1:
            self._move_node_to_front(node)
            return node.val
        return node

    def put(self, key: int, value: int) -> None:
        if key in self.node_dict:
            node = self.node_dict.get(key)
            node.val = value
            self._move_node_to_front(node)
        else:
            node = LRUCacheNode(key, value)
            self._add_node_to_front(node)
            self.node_dict.update({key: node})
            self.nums += 1 
            
            if self.nums > self.capacity:
                self._delete_tail()
                self.nums -= 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
