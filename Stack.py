class Stack:
    def __init__(self):
        self._items = []

    def push(self, pet_id):
        self._items.append(pet_id)

    def pop(self):
        if self.is_empty():
            return None
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0