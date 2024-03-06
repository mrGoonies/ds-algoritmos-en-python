def quicksort(lst: list) -> list:

    # Aplicando caso base
    if len(lst) < 2:
        return lst
    
    # elegimos elemento pivote
    pivot = lst[0]
    
    # Creamos una lista que almacena los elementos que son menores o iguales al caso pivote
    less = [i for i in lst[1:] if i <= pivot]

    # Creamos una lista que almacena los elementos que son mayores al caso pivote
    greater = [i for i in lst[1:] if i > pivot]
    
    # Concatenamos de forma ordenada los elementos ordenados de una lista base
    return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == "__main__":
    print(quicksort([10, 5, 2, 3]))
