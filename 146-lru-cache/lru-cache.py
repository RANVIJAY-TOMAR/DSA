'''
key idea:
take advantage of fact that python's dict is ordered in terms of insertion order.  bottom is oldest, top is newest.
to 'touch' a key to reset it and indicate it's been used: pop it then put it back in.
'''

class LRUCache:

    def __init__(self, cap: int):
        self.cap = cap
        self.m = {}

    def get(self, key: int) -> int:
        if key not in self.m:
            return -1

        # fetch value if it exists, delete it so you get rid of first insertion order. 
        # then add it which puts it at the top since it doesnt exist in the dict
        temp = self.m.pop(key)
        self.m[key] = temp
        return temp
        

    def put(self, key: int, value: int) -> None:
        # delete key if exists
        if key in self.m:
            self.m.pop(key)

        # then add it which puts it at the top since it doesnt exist in the dict
        self.m[key] = value

        # len will only ever be at most 1 over capacity, since we check every time
        if len(self.m) > self.cap:
            # pop the oldest key
            self.m.pop(next(iter(self.m)))


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)