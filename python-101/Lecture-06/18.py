inventory = [
    ["Apple", 50, 0.75],
    ["Banana", 100, 0.50,],
    ["Orange", 75, 0.80]
]
def update_inventory(inventory,item_name,quantitu_slod):
    for item in inventory :
        item[0] == quantitu_slod
        item[1] -= item_name
        return
    print(f"สินค้าคงเหลือ,'{item_name}'")