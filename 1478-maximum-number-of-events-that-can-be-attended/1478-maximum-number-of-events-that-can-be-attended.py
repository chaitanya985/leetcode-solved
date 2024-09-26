import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:

        events.sort(key=lambda x: x[0])
        
        max_heap = []
        
        day = 0
        
        count = 0
        
        i = 0
        
        n = len(events)

        while i < n or max_heap:
        
            if not max_heap:
        
                day = events[i][0]
        
            while i < n and events[i][0] <= day:
        
                heapq.heappush(max_heap, events[i][1])
        
                i += 1
        
            heapq.heappop(max_heap)
        
            count += 1
        
            day += 1
        
            while max_heap and max_heap[0] < day:
        
                heapq.heappop(max_heap)

        return count
        