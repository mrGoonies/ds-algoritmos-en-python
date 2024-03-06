def sum_arr_values(lst: list[int]) -> int:
    total: int = 0

    for element in lst:
        total += element

    return total

# Implementación con recursión
def sum_recursion(lst: list[int], value: int=0) -> int:
    current_value: int = value
    
    if len(lst) <= 0:
        return current_value

    current_value += lst.pop()
    #print(current_value)

    return sum_recursion(lst, current_value)

def get_higher_num(lst: list[int], current_value=0, current_counter: int = 0) -> int:
    higher_num = current_value
    counter = current_counter

    if not lst or counter == len(lst):
        return higher_num

    if lst[counter] > higher_num:
        higher_num = lst[counter]

    counter += 1

    return get_higher_num(lst, higher_num, counter)


if __name__ == "__main__":
    print("Resultado de una función sin recursión:")
    print("\t>> ", sum_arr_values([1, 2, 3, 4, 5]))
    
    print("Resultado de una función con recursión:")
    print("\t>> ", sum_recursion([1, 2, 3, 4, 5]))

    print("Resultado del valor más alto de una lista usando recursión es:")
    print("\t>> ", get_higher_num([10, -5, 100, 3, -23, 1]))

