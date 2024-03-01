# Recursion

Es una técnica el cual varios algoritmos hacen uso de ella, además de ser una técnica bastante interesante (sobretodo para iniciantes) puede llegar a ser controversial debido a que tienen una gran fanaticada como varios detractores.

La recursión en palabras simples siginifica que una función se llama asi misma, por ejemplo, quieres validar un input pero el usuario ingreso dato erróneos, en vez que la función se llame nuevamente o agreges más código para que vuélva a solicitar el input y validarlo, retornas (en el caso que no se cumple) la misma función y así ahorras código duplicado del primer enfoque. Tal vez la recursión no es el método con mejor rendimiento en comparación a un loop tradicional o al primer enfoque pero para un programador es más valorable la legibilidad y simpleza sobre la complejidad forzada. Recuerda utilizar correctamente la recursividad.


## Consideraciones

1. Al declarar una función recursiva, es altamente recomendado y obligación aplicar una condición para que la función sepa cuando debe dejar de llamarse así misma.

2. Las funciones recursivas pueden utilizar más cómputo que una función normal.
