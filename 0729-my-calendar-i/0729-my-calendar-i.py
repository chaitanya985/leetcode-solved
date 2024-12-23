from sortedcontainers import SortedDict

class MyCalendar:
    
    def __init__(self):
        
        self.sd = SortedDict()

    def book(self, start: int, end: int) -> bool:
        
        idx = self.sd.bisect_right(start)

        if idx < len(self.sd) and end > self.sd.values()[idx]:
            
            return False
        
        self.sd[end] = start
        
        return True