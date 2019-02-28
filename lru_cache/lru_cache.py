import sys
sys.path.insert(0, 'C:/Users/McKay/Documents/GitHub/Data-Structures/doubly_linked_list')

from doubly_linked_list import DoublyLinkedList

class LRUCache:
    def __init__(self, limit=10):
        self.dictionary = {}
        self.limit = limit
        self.size = 0
        self.node_refs = {}
        self.priority = DoublyLinkedList()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the top of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache. 
    """
    def get(self, key):
        if not key in self.dictionary:
            return None
        else:
            self.priority.move_to_front(self.node_refs[key])
            self.print_self()
            return self.dictionary[key]

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
        # If key is already in dictionary, just change it and move it to most-recently-used
        if key in self.dictionary:
            print("Flag1")
            self.dictionary[key] = value
            self.priority.move_to_front(self.node_refs[key])
            print("Flag2")
        # Otherwise, it needs to be added to the dictionaries and the priority
        else:
            self.dictionary[key] = value
            self.priority.add_to_head(key)
            self.node_refs[key] = self.priority.head
            # If the cache wasn't full, just update its new size
            if self.size < self.limit:
                self.size += 1
            # Otherwise, the cache is now over-full and the LRU needs to be deleted
            else:
                oldest_key = self.priority.tail.value
                self.priority.remove_from_tail()
                self.node_refs.pop(oldest_key)
                self.dictionary.pop(oldest_key)
        self.print_self()

    def print_self(self):
        print(f'dictionary: {self.dictionary}')
        print(f'node_refs: {self.node_refs}')
        print("Priorities:")
        p = self.priority.head
        while p:
            print(p.value)
            p = p.next
        print()

