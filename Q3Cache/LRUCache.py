from collections import deque

class LRUCache(object):
    def __init__(self, capacity = 10, dictitems = None):
        self.capacity = capacity
        self.lruList = deque()  #doubly linked list used to keep track of lru objects
        self.items = {}
        if dictitems:
            self.items.update(dictitems)

    def __setitem__(self, key, value):
        if self.lruList.__contains__(key):
            raise ValueError("Key %s is already present" %key)

        if len(self.items)+1 > self.capacity: #cache is full, remove lru item
            lruItemKey = self.lruList.popleft()
            del self.items[lruItemKey]

        self.items[key] = value

        # append the key of the item to the end of the list to indicate it is the most recently used
        self.lruList.append(key)

    def __getitem__(self, key):
        if key not in self.lruList:
            raise ValueError("Key %s does not exist" %key) #cache miss, to be caught by calling method

        #Re-append the key to the most recently used spot
        self.lruList.remove(key)
        self.lruList.append(key)
        return self.items[key]

    def __delitem__(self, key):
        if key not in self.lruList:
            raise ValueError("Key %s does not exist" %key) #cache miss, to be caught by calling method

        self.lruList.remove(key)
        del self.items[key]