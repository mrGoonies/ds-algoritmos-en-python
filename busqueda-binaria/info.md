# Búsqueda Binaria

Es un algoritmo que resuelve el problema de búsqueda lineal o la búsqueda tradicional (acceder uno por uno a los elementos de un arreglo o lista) de una manera bastante eficiente y rápida. Aunque se deben cumplir ciertas restricciones para que este algoritmo funcione de manera correcta:

1. Los elementos de la lista deben estar ordenados.
2. No deben existir valores repetidos.

Ahora, ¿cómo funciona la búsqueda binaria? Este algoritmo divide la lista en dos mitades y verifica si el elemento que se está buscando se encuentra en la mitad de la lista, si no está, se pregunta:

**¿El elemento actuale es mayor o menor que el elemento que se está buscando?**

Si el elemento actual es mayor, se descarta la mitad de la lista que contiene el elemento actual y sus sucesiones, si el elemento actual es menor, se descarta la mitad de la lista que contiene el elemento actual y sus predecesores. Este proceso se repite hasta que el elemento que se está buscando sea encontrado o la lista se quede sin elementos.

Una vez encontrado el elemento, se retorna el índice en el que se encuentra dentro de la lista, de lo contrario, se retorna `None` o `null`.

## Cálcular tiempo de ejecución
Para cálcular el tiempo de ejecución de este algoritmo, haremos uso de logaritmos, en este caso en base 2. La fórmula para cálcular el tiempo de ejecución de la búsqueda binaria es:

\begin{equation}
\log_2 n = x
\end{equation}

Donde `n` es el número de elementos en la lista y `x` es el número de veces que se debe dividir la lista para encontrar el elemento que se está buscando.

## Ejemplo
Supongamos que tenemos la siguiente lista:

```python
lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]

# Obtenemos el valor de n para nuestro logaritmo:
valor_n: int = len(lista)
```

Ahora, cálculemos el tiempo de ejecución de la búsqueda binaria:

\begin{equation}
\log_2 25 = 4.64
\end{equation}

Esto nos indica que para encontrar un elemento en una lista de 25 elementos, se deben realizar 4.64 o 5 divisiones en la lista para encontrar el elemento que se está buscando. En cambio, si queremos implementar laa búsqueda tradicional, esto nos tomaráa 25 pasos para encontrar el elemento que se está buscando.
