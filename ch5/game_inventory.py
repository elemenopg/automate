stuff = {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12}

def display_inventory(inv: dict[str,int]):
    print('Inventory:')
    item_total = 0
    for item, quant in inv.items():
        item_total += quant
        print(f'{quant} {item}')
    print(f'Total number of items: {item_total}')

# display_inventory(stuff)

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
current_inv = {'gold coin': 42, 'rope': 1}

def add_to_inventory(inv: dict[str,int], new_items: list) -> dict[str,int]:
    for item in new_items:
        if item in inv:
            inv[item] += 1
        else:
            inv[item] = 1
    return inv

add_to_inventory(current_inv, dragon_loot)
display_inventory(current_inv)
