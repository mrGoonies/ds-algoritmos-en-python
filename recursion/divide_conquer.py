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


if __name__ == "__main__":
    print("Resultado de una función sin recursión:")
    print("\t>> ", sum_arr_values([1, 2, 3, 4, 5]))
    
    print("Resultado de una función con recursión:")
    print("\t>> ", sum_recursion([1, 2, 3, 4, 5]))

