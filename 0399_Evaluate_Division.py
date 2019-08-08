class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        equation_map = collections.defaultdict(set)
        
        for idx, equation in enumerate(equations):
            equation_map[equation[0]].add((equation[1], values[idx]))
            equation_map[equation[1]].add((equation[0], 1.0/values[idx]))
        
        answers = []
        for query in queries:
            answers.append(self.calculate(query, equation_map))
        return answers
    
    
    def calculate(self, query, equation_map):
        queue = [(query[0], 1.0)]
        visited = set()
        
        while queue:
            next_queue = []
            
            for (A, val_A) in queue:
                for (B, val_B) in equation_map[A]:
                    if B not in visited:
                        val = val_A * val_B
                        if B == query[1]:
                            return val
                        next_queue.append((B, val))
                        visited.add(B)
            
            queue = next_queue
        return -1.0
