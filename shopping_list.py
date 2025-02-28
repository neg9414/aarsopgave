class ShoppingList:
    """
    En klasse, der repræsenterer en indkøbsliste.
    """

    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    def get_items(self):
        return self.items


def main():
    shopping_list = ShoppingList()
    print("""
    Velkommen til din indkøbsliste!
    Sådan bruger du programmet:
    - Skriv '+ antal vare' for at tilføje en vare (f.eks. '+ 2 mælk')
    - Skriv '- vare' for at fjerne en vare (f.eks. '- mælk')
    - Skriv 'list' for at se din nuværende indkøbsliste
    - Skriv 'exit' for at afslutte programmet
    """)
    
    while True:
        command = input("> ").strip()
        
        if command.lower() == "exit":
            break
        elif command.startswith("+"):
            parts = command[1:].strip().split(" ", 1)
            quantity = int(parts[0])
            item = parts[1]
            shopping_list.add_item(item, quantity)
            print(f"Tilføjet: {quantity} x {item}")
        elif command.startswith("-"):
            item = command[1:].strip()
            shopping_list.remove_item(item)
            print(f"Fjernet: {item}")
        elif command.lower() == "list":
            items = shopping_list.get_items()
            print("\nIndkøbsliste:")
            for item, quantity in items.items():
                print(f"{quantity} x {item}")
            print()
        else:
            print("Ugyldig kommando. Prøv igen.")

if __name__ == "__main__":
    main()
