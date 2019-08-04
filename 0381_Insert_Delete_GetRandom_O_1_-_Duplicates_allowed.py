class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.total_count = 0
        self.val_counter = collections.Counter()
        

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.total_count += 1
        self.val_counter[val] += 1
        return self.val_counter[val] == 1
            

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if self.val_counter[val] == 0:
            return False
        else:
            self.total_count -= 1
            self.val_counter[val] -= 1
            return True
            

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        random_idx = random.randint(1, self.total_count)
        for val, count in self.val_counter.items():
            random_idx -= count
            if random_idx <= 0:
                return val


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
