class PriorityQueue:
    def __init__(self):
        self._items = []

    def enqueue(self, pet_node):
        if pet_node.severity == 1:
            self._items.insert(0, pet_node)
            print(f"\n  EMERGENCY! {pet_node.name} has been placed at the FRONT of the queue!")
        else:
            pos = len(self._items)
            for i, p in enumerate(self._items):
                if p.severity > pet_node.severity:
                    pos = i
                    break
            self._items.insert(pos, pet_node)

    def dequeue(self):
        if self.is_empty():
            return None
        return self._items.pop(0)

    def remove_by_id(self, pet_id):
        for i, p in enumerate(self._items):
            if p.pet_id == pet_id:
                self._items.pop(i)
                return True
        return False

    def display(self):
        if self.is_empty():
            print("\n  Consultation queue is empty.")
            return
        print("\n" + "─" * 60)
        print(f"  {'#':<5} {'Pet Name':<15} {'Breed':<15} {'Owner':<15} {'Sev'}")
        print("─" * 60)
        for i, p in enumerate(self._items, 1):
            tag = " ← NEXT" if i == 1 else ""
            print(f"  {i:<5} {p.name:<15} {p.breed:<15} {p.owner:<15} {p.severity}{tag}")
        print("─" * 60)
        print(f"  Pets waiting: {len(self._items)}")

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)