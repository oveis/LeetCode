class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        tickets.sort(reverse = True)
        flights = collections.defaultdict(list)
        for start, end in tickets:
            flights[start].append(end)
        journey = []
        
        def visit(airport):
            while flights[airport]:
                visit(flights[airport].pop())
            journey.append(airport)
            
        visit('JFK')
        return journey[::-1]
