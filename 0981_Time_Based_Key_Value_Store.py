class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_to_values = collections.defaultdict(list)
        self.key_to_times = collections.defaultdict(list)
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.key_to_values[key].append(value)
        self.key_to_times[key].append(timestamp)
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        idx = bisect.bisect_right(self.key_to_times[key], timestamp)
        if idx == 0:
            return ''
        return self.key_to_values[key][idx - 1]
    

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
