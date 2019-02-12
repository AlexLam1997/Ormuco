import hashlib
import bisect
from Q3Cache import LRUCache

'''
Defines a consistent hash circle used to distribute the storage load among multiple caches.
Allows for easy addition or removal of caches from the distributed system. 
Guards against the sudden removal of caches from the system due to cache failures as only 
information in the removed cache is invalidated instead of the whole cache as in a traditional cache


In consistent hashing both the caches and the objects to be cached are hashed and mapped to a circle 
such that the values wrap around. There will then be objects points and cache points mapped to the hash circle.
To determine in which cache an object belongs we move clockwise along the circle until we hit a cache point. The 
first cache point hit is the cache in which the object belongs. When a cache, or a node, is added to the circle,
many replicas of that node are also added along the circle in order to achieve a more uniform distribution of 
objects among the caches. 

The consistent hash circle implements a dictionary interface for easy addition of nodes (caches) 
'''
class ConsistentHashCircle(object):

    def __init__(self, replicas = 25):
        self.replicas = replicas
        self.keys = []
        self.nodes = {}

    def __hash(self, key):
        return hashlib.md5(key.encode('utf-8')).hexdigest()

    '''
    Given a node key, returns a iterable of replica hash values 
    Returns replicaNumber number of replicas.
    '''
    def _duplicate_node_hashes(self, nodekey):
        return (self.__hash("%s: %s" % (nodekey, replicaNumber))
                for replicaNumber in range(self.replicas))

    ''' 
    Adding a node(which is used as a lruCache here) to the consistent hash circle 
    this adds replicas of the node to multiple locations on the circle in 
    order to distribute the load on the different nodes     
    '''
    def __setitem__(self, nodekey, node):
        for hash in self._duplicate_node_hashes(nodekey):
            self.nodes[hash] = node
            bisect.insort(self.keys, hash)

    '''
    Delete all nodes given the key associated to the node referenced
    '''
    def __delitem__(self, nodekey):
        for hash in self._duplicate_node_hashes(nodekey):
            del self.nodes[hash]
            keyindex = bisect.bisect_left(self.keys, hash)
            del self.keys[keyindex]

    '''
    Get a node for an object. The hash value of the object is used 
    to find the node in the map. If there is no node at this hash value 
    (most of the time) the next closest node is found using bisect. 
    Bisect finds the object hash given the list is sorted, so if the index 
    found is at the end of the list so the object hash is greater than the greatest 
    hashed key then returns the lowest hashed node
    '''
    def __getitem__(self, object):
        objecthash = self.__hash(object)
        keyindex = bisect.bisect(self.keys, objecthash)
        if keyindex == len(self.keys):
            keyindex = 0
        return self.nodes[self.keys[keyindex]]

    '''
    Defines easy to use cache saving method which automatically sets up a new 
    cache as a node in the circle if no nodes are defined 
    '''
    def addtocache(self, key, value):
        if not self.nodes: #no caches added to the hash circle
            self.__setitem__("Cache1", LRUCache.LRUCache())
        cache = self.__getitem__(key)
        cache[key] = value





