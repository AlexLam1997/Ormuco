from unittest import TestCase
from Q3Cache import LRUCache

class CacheTest(TestCase):

    def setUp(self):
        self.lrucache = LRUCache.LRUCache(3)

    def test_savetocache(self):
        keys = ["k1","k2","k3","k4"]
        values = ["v1","v2","v3","v4"]

        #Since cache has max of 3 items cache should have k2, k3 and k4
        for i in range (4):
            self.lrucache[keys[i]] = values[i]

        self.assertEqual(list(self.lrucache.items.keys()), keys[1:4])
        self.assertEqual(list(self.lrucache.items.values()), values[1:4])
