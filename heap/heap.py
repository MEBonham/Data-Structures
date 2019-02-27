class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):

        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        # Special cases if the heap is very small
        if len(self.storage) == 0:
            return None
        if len(self.storage) == 1:
            temp, self.storage = self.storage[0], []
            return temp
        # Default case for bigger heaps
        temp, self.storage[0] = self.storage[0], self.storage.pop()
        self._sift_down(0)
        return temp

    def get_max(self):
        if len(self.storage) == 0:
            return None
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        # Base case: we have reached the root of the tree
        if index == 0:
            return
        # Recursive case: check about bubbling up 1 spot, then call bubble_up again if so
        parent_index = (index - 1) // 2
        if self.storage[index] > self.storage[parent_index]:
            self.storage[index], self.storage[parent_index] = self.storage[parent_index], self.storage[index]
            self._bubble_up(parent_index)

    def _sift_down(self, index):
        left_child = index * 2 + 1
        right_child = index * 2 + 2
        # Base case: leaf node can't sift_down any further
        if left_child >= len(self.storage):
            return
        # By default, compare with the left-child value:
        compare_index = left_child
        # But if right child exists and is greater, switch to comparing to it:
        if right_child < len(self.storage) and self.storage[right_child] > self.storage[left_child]:
            compare_index = right_child
        # Recursive case: check about sifting down 1 spot, then call sift_down again if so
        if self.storage[compare_index] >= self.storage[index]:
            self.storage[index], self.storage[compare_index] = self.storage[compare_index], self.storage[index]
            self._sift_down(compare_index)


