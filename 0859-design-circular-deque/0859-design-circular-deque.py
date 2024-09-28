class MyCircularDeque:

    def __init__(self, k):
 
        self.queue = []
        
        self.size = k
        
        self.front = 0
        
        self.rear = 0

    def insertFront(self, value):

        if not self.isFull():
            
            self.queue.insert(0, value)
            
            self.rear += 1
            
            return True
    
        else:
    
            return False
        

    def insertLast(self, value):

        if not self.isFull():
    
            self.queue.append(value)
    
            self.rear += 1
    
            return True
    
        else:
    
            return False

    def deleteFront(self):

        if not self.isEmpty():
    
            self.queue.pop(0)
    
            self.rear -= 1
    
            return True
        else:
    
            return False

    def deleteLast(self):

        if not self.isEmpty():
    
            self.queue.pop()
    
            self.rear -= 1
    
            return True
        else:
    
            return False

    def getFront(self):

        if self.isEmpty():
    
            return -1
    
        else:
    
            return self.queue[self.front]

    def getRear(self):

        if self.isEmpty():
    
            return -1
    
        else:
    
            return self.queue[self.rear -1]

    def isEmpty(self):

        return self.front == self.rear

    def isFull(self):

        return self.rear - self.front == self.size
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()