color_list = ["blue", "teal", "green"]
print("Color list:")
print(", ".join(color_list))

position = int(input("Input position: "))
if position <= len(color_list):
    print(f"Color at position {position}: {color_list[position-1]}")
else:
    print("Invalid position")

color_list = ["blue", "teal", "green"]
print("Color list:")
print(", ".join(color_list))

item_to_delete = input("Item to delete: ")
if item_to_delete.isdigit():
    index = int(item_to_delete)
    if index <= len(color_list) and index > 0:
        del color_list[index-1]
        print("New color list: " + ", ".join(color_list))
    else:
        print("Invalid position")
else:
    if item_to_delete in color_list:
        color_list.remove(item_to_delete)
        print("New color list: " + ", ".join(color_list))
    else:
        print("Color not found")