class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class KeyValueDataStructure:

    def __init__(self):
        self.size = 19997
        self.multiplicative_factor = 31
        self.storage = [None] * self.size
        self.used_keys = []

    def hash(self, key):
        return (key * self.multiplicative_factor) % self.size

    def set(self, key, value):
        if not isinstance(key, int):
            print("Key is not an integer.")
            return

        if not isinstance(value, str):
            print("Value is not a string.")
            return

        index = self.hash(key)

        head = self.storage[index]

        if not head:
            self.storage[index] = Node(key, value)
            self.used_keys.append(index)
        else:
            prev = None
            while head:
                if head.key == key:
                    head.value = value
                    return

                prev, head = head, head.next

            prev.next = Node(key, value)

    def get(self, key):
        if not isinstance(key, int):
            print("Key is not an integer.")
            return

        index = self.hash(key)

        head = self.storage[index]

        while head:
            if head.key == key:
                return head.value

            head = head.next

        return

    def display(self):
        res = []
        for index in self.used_keys:
            node = self.storage[index]
            while node:
                res.append((node.key, node.value))
                node = node.next
        return res
