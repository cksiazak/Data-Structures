import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.storage = dict()
        self.dll = DoublyLinkedList()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        # check if key is in self.storage
        if key in self.storage:
            # create node based on the key in storage
            node = self.storage[key]
            # use move_to_end method on dll to move to end
            self.dll.move_to_end(node)
            # return that value
            return node.value[1]
        else:
        # if it isn't, return nothing
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        # check if key is in self.storage
        if key in self.storage:
            # create node using the key in storage
            node = self.storage[key]
            # store a touple on node's value
            node.value = (key, value)
            # use dll method move_to_end and pass the node in
            self.dll.move_to_end(node)
            return
        
        # if key is not in self.storage
        # check if size is more than or equal to limit
        if self.size >= self.limit:
            # if it is, delete the oldest value
            del self.storage[self.dll.head.value[0]]
            # remove from head
            self.dll.remove_from_head()
            # decrease size of our storage
            self.size -= 1
        
        # add the key/val touple to tail
        self.dll.add_to_tail((key, value))
        # set the node to the key in storage
        self.storage[key] = self.dll.tail
        # increase size
        self.size += 1
