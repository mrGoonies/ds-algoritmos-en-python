# Quick Sort

Es un algoritmo de ordenamiento mucho más rápido que **selection sort** u **ordenamiento por selección**. Este algoritmo usa *Divide y conquistarás**.

## Funcionamiento

Este algoritmos funciona de una forma peculiar. En base a una lista o arreglo, debelos elegir un elemento (el que desees) y ese elemento lo llamaremos *pivote* o *pivot*. Luego crearemos dos sub-listas o arreglos, una de estas sublistas almacenará los elementos que sean menores e igual al pivote, y otra lista que contenga elementos mayores al pivote. Este proceso se aplicará para cada sub-lista de forma recursiva (por eso es importante conocer recursividad). Una vez ordenadas las sublistas, haremos una concatenación entre los elementos menores + pivot + elementos mayores al pivot. Puedes analizar el código de implementación que se encuentra en esta misma ruta.

*El tiempo de ejeción de este tipo de algoritmos es algo difícil de cálcular debido a que dependerá netamente del pivote seleccionado*




