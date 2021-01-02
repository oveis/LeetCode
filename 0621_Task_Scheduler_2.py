class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_order = []
        counter = Counter(tasks)
        total_tasks = len(tasks)
        
        while counter:
            for idx, (task, _) in enumerate(counter.most_common()):
                if idx > n:
                    break
                    
                task_order.append(task)
                counter[task] -= 1
                
                if counter[task] == 0:
                    del counter[task]
            else:
                if counter:
                    task_order += ['idle'] * (n - idx)
        
        return len(task_order)
