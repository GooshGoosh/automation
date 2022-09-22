#!/usr/bin/env python3

# gameInventory.py - Stores a dictionary of items in a game inventory where the keys are string values describing the item and the value is an integer.
# The program will take the dictionary of items and print out the amount of each item as well as the total number of items.
# Then, the program will add a list of items to the inventory, creating new keys and updating values as necessary which will then be displayed to the user.


bag = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def display_inventory(inventory):
    print('\nInventory:')
    itemTotal = 0
    for k, v in inventory.items():
        itemTotal += v
        print(f'{v} {k}')
    print(f'\nTotal number of items: {itemTotal}\n')
    
    
def add_to_inventory(inventory, itemList):
    for item in itemList:
        if item in inventory:
            inventory[item] += 1
        elif item not in inventory:
            inventory[item] = 1
    return inventory


def main():
    display_inventory(bag)
    bag = add_to_inventory(bag, loot)
    display_inventory(bag)


if __name__ == "__main__":
    main()
