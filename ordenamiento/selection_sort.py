
def find_smallest_item(lst: list) -> int:
    smallest = lst[0]
    smallest_index = 0

    for i in range(0, len(lst)):
        if lst[i] < smallest:
            smallest_index = i

    return smallest_index

def selection_sort(lst: list) -> list:
    new_list = list()
    copied_arr = list(lst)

    for i in range(len(copied_arr)):
        smallest = find_smallest_item(copied_arr)
        new_list.append(copied_arr.pop(smallest))

    return new_list

if __name__ == "__main__":
    print(selection_sort([5, 3, 6, 2, 10]))
