""" Implementación del algoritmo de búsqueda binaria """

from typing import Optional


def binary_search(lst: list, target: int) -> Optional[int]:
    # Inicializar los valores de low y high que representan los índices del primer y último elemento de la lista
    low, high = 0, len(lst) - 1

    while low <= high:
        # Calcular el índice medio
        mid: int = (low + high) // 2

        # Obtener el valor del elemento medio
        guess = lst[mid]

        if guess == target:
            return mid
        elif guess > target:
            # Si el valor del elemento medio es mayor que el objetivo, se actualiza el valor de high
            # para que sea el índice anterior al elemento medio y así se descarte la mitad superior de la lista
            high = mid - 1
        else:
            # Si el valor del elemento medio es menor que el objetivo, se actualiza el valor de low
            # para que sea el índice siguiente al elemento medio y así se descarte la mitad inferior de la lista
            low = mid + 1

    return None

if __name__ == "__main__":
    numbers: list[int] = [i for i in range(1, 101)]
    target: int = 41
    result: int = binary_search(numbers, target)

    if result is not None:
        print(f"El número {target} se encuentra en la posición {result} de la lista.")

    else:
        print(f"El número {target} no se encuentra en la lista.")
