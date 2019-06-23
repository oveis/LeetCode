class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.key_queue = []
        self.key_value_dict = dict()
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key_value_dict:
            return -1
        
        self.key_queue.remove(key)
        self.key_queue.append(key)

        return self.key_value_dict[key]
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.key_value_dict:
            self.key_queue.remove(key)
            
        self.key_queue.append(key)
        self.key_value_dict[key] = value
        
        if len(self.key_queue) > self.capacity:
            del_key = self.key_queue.pop(0)
            self.key_value_dict.pop(del_key)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
