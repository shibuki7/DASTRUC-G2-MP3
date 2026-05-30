from pets import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, pets):
        new_node = Node(pets)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head

        if current is None:
            print(f"\n{'=' * 20}")
            print("\nNo pets registered")
            print(f"\n{'=' * 20}")
            return

        while current:
            pets = current.pets
            print(f"\n{'=' * 100}")
            print(f"\nPet ID: {pets.pet_id} | "
                  f"Pet Name: {pets.pet_name} | "
                  f"Breed: {pets.breed} | "
                  f"Owner Name: {pets.owner_name} | "
                  f"Severity Level: {pets.severity} | ")
            print(f"\n{'=' * 100}")
            current = current.next

    def search(self, pet_id):
        current = self.head

        while current:
            if current.pets.pet_id == pet_id:
                return current.pets
            current = current.next

        return None

    def delete(self, pet_id):
        current = self.head
        previous = None

        while current:
            if current.pets.pet_id == pet_id:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return True
            previous = current
            current = current.next

        return False
