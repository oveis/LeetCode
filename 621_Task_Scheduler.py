class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        tasks_count = [0] * 26
        for task in tasks:
            tasks_count[ord(task) - ord('A')] += 1
        tasks_count.sort(reverse=True)
        
        max_val = tasks_count[0] - 1
        num_idles = max_val * n
        
        for count in tasks_count[1:]:
            num_idles -= min(count, max_val)
        
        return len(tasks) + num_idles if num_idles > 0 else len(tasks)
