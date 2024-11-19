class MyHashMap:

    def __init__(self):

        self.head=[-1]*10000001
        
    def put(self, key: int, value: int) -> None:

        self.head[key]=value
        
    def get(self, key: int) -> int:

        return self.head[key]
        
    def remove(self, key: int) -> None:

        self.head[key]=-1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)