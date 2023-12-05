def separator(some_list):
    if len(some_list) == 0:
        print("This list is empty.")
    else:
        for i in range(len(some_list)):
            if i == len(some_list) - 1:
                print(f"and {some_list[i]}")
            else:
                print(f"{some_list[i]}, ", end="")


my_list = []

while True:
    list_item = input("Please add to your list, or enter nothing to finish.\n")
    if list_item == "":
        break
    else:
        my_list.append(list_item)

separator(my_list)