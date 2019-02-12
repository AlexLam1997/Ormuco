from unittest import TestCase
from Q3Cache import LRUCache
from Q3Cache import ConsistentHashCircle

class ConsistentHashTest(TestCase):
    def setUp(self):
        self.ch = ConsistentHashCircle.ConsistentHashCircle()

        cache1 = LRUCache.LRUCache()
        cache2 = LRUCache.LRUCache()

        self.ch["node1"] = cache1
        self.ch["node2"] = cache2

        node = self.ch["data1"]
        node ["testkey"] = "test value"

    def test_retrievefromcache(self):
        cache = self.ch["data1"]
        self.assertEqual(cache["testkey"], "test value")

    def test_savetocache(self):
        self.ch.addtocache("key3", "value3")

        cache = self.ch["key3"]
        self.assertEqual(cache["key3"], "value3")



