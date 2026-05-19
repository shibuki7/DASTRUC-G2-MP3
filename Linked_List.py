from Pet_Node import PetNode
class LinkedList:
    def __init__(self):
        self.head  = None
        self.count = 0

    def insert(self, pet_node):
        if self.head is None:
            self.head = pet_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = pet_node
        self.count += 1

    def delete(self, pet_id):
        curr = self.head
        prev = None
        while curr:
            if curr.pet_id == pet_id:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                curr.next = None
                self.count -= 1
                return curr
            prev = curr
            curr = curr.next
        return None

    def search(self, pet_id):
        curr = self.head
        while curr:
            if curr.pet_id == pet_id:
                return curr
            curr = curr.next
        return None

    def update(self, pet_id, name=None, breed=None, owner=None, severity=None):
        node = self.search(pet_id)
        if node is None:
            return False
        if name     is not None: node.name     = name
        if breed    is not None: node.breed    = breed
        if owner    is not None: node.owner    = owner
        if severity is not None: node.severity = severity
        return True

    def display(self):
        if self.head is None:
            print("\n  No pets registered yet.")
            return
        print("\n" + "─" * 60)
        print(f"  {'ID':<8} {'Pet Name':<15} {'Breed':<15} {'Owner':<15} {'Sev'}")
        print("─" * 60)
        curr = self.head
        while curr:
            print(f"  {curr.pet_id:<8} {curr.name:<15} {curr.breed:<15} {curr.owner:<15} {curr.severity}")
            curr = curr.next
        print("─" * 60)
        print(f"  Total registered: {self.count}")

    def is_empty(self):
        return self.head is None