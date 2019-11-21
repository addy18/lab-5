import math

# PART A
class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        temp = self.tail
        temp.next = node
        node.prev = temp
        self.tail = node
        node.next = None

    def relocate(self, node):
        if node is self.tail:
            return
        if node is self.head:
            n = self.head.next
            n.prev = None
            self.head = n
            self.insert_at_end(node)
        else:
            temp = node.prev
            temp.next = node.next
            tt = node.next
            tt.prev = temp
            self.insert_at_end(node)

    def delete_start(self):
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        temp = self.head
        temp.prev = None


class LRU:
    def __init__(self, max_cap):
        self.LRU = {}
        self.max_cap = max_cap
        self.list = DoublyLinkedList()
        self.size = 0

    def get(self, key):
        if key in self.LRU:
            self.list.relocate(self.LRU[key])
            return self.LRU[key]
        else:
            return -1

    def put(self, key, value):
        node = Node(value, key)
        if key not in self.LRU:
            if self.size != self.max_cap:
                self.list.insert_at_end(node)
                self.size += 1
            else:
                self.list.delete_start()
                self.list.insert_at_end(node)
        else:
            self.get()

    def size(self):
        return self.size

    def max_capacity(self):
        return self.max_cap

    def print(self):
        n = self.list.head
        while n is not None:
            print(n.data, n.key)
            n = n.next


# PART B
class MaxHeap:
    def __init__(self):
        self.tree = []

    def is_empty(self):
        return len(self.tree) == 0

    def parent(self, i):
        if i == 0:
            return -math.inf
        return self.tree[(i-1) // 2]

    def left_child(self, i):
        child = 2 * i + 1
        if child >= len(self.tree):
            return -math.inf
        return self.tree[child]

    def right_child(self, i):
        child = 2 * i + 2
        if child >= len(self.tree):
            return -math.inf
        return self.tree[child]

    def insert(self, item):
        self.tree.append(item)
        self._percolate_up(len(self.tree) - 1)

    def _percolate_up(self, i):
        if i == 0:
            return
        parent_index = (i - 1) // 2
        if self.tree[parent_index] < self.tree[i]:
            self.tree[i], self.tree[parent_index] = self.tree[parent_index], self.tree[i]
            self._percolate_up(parent_index)

    def extract_max(self):
        if len(self.tree) < 1:
            return None
        if len(self.tree) == 1:
            return self.tree.pop()
        root = self.tree[0]
        self.tree[0] = self.tree.pop()
        self._percolate_down(0)

        return root

    def _percolate_down(self, i):
        if self.tree[i] >= max(self.left_child(i), self.right_child(i)):
            return
        max_child_index = 2 * i + 1 if self.left_child(i) > self.right_child(i) else 2 * i + 2
        self.tree[i], self.tree[max_child_index] = self.tree[max_child_index], self.tree[i]
        self._percolate_down(max_child_index)


def heap_sort(a_lst):
    h = MaxHeap()
    for a in a_lst:
        h.insert(a)
    i = 0
    while not h.is_empty():
        a_lst[i] = h.extract_max()
        i += 1


def frequent(string, k):
     dict = {}
    alist = list()
    words = list()
    word_and_value = list()
    same_value = list()
    visited = set()

    # puts the string of words into dictionary then is sorted in a heap sort
    for i in range(len(string)):
        if string[i] in dict:
            dict[string[i]] += 1
        else:
            dict[string[i]] = 1
    for word, value in dict.items():
        alist.append(value)
    heap_sort(alist)
    print("dictionary", dict)
    # print("alist", alist)

    # checks if k is valid
    if k > len(alist) or k < 0:
        print("error k is bigger than the string of words")
        return

    for value in alist:
        for word, key in dict.items():
            # looks for words with the same number of occurrences
            if value == key and word not in visited:
                same_value.append(word)
                visited.add(word)
        same_value.sort()
        # sorts into heap
        for m in range(len(same_value)):
            word_and_value.insert(-2, (same_value[m], value)) # -2
            words.append(same_value[m])
        same_value.clear()

    # print("word and value", word_and_value)
    # print("words", words)

    for i in range(k):
        print(word_and_value[i])
        # print(words[i])


def main():
    a = LRU(3)
    a.put("A", 2)
    a.put("B", 3)
    a.put("C", 9)
    a.put("D", 10)
    a.put("E", 130)

    a1 = LRU(4)
    a1.put("add", 5)
    a1.put("bob", 6)
    a1.put("hill", 8)
    a1.put("love", 10)
    a1.put("princess", 100)
    a1.put("hi", 24)
    a1.put("dog", 78)

    print("PART A -----------------")
    print("TEST ONE")
    a.print()
    print("\nTEST TWO")
    a1.print()
    print("------------------------")

    s = ["hi", "heloo", "lol", "hiosd", "hiosd", "lol", "hello", "dog", "dog", "dog", "dog", "dog"]
    s2 = ["adds", "lol", "cat", "cat", "dog", "jax", "jax", "jax", "lol", "dog", "dog", "lol"]

    print("PART B -----------------")
    print("TEST ONE")
    frequent(s, 8)

    print("\nTEST 2")
    frequent(s2, 4)
    print("------------------------")


main()
