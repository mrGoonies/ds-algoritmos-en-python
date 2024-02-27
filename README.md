# Algoritmos y Estructuras de datos en Python

Python es uno de los lenguajes de programación más utilizados por programadores y empresas, esto se debe a su facilidad de uso y a su gran avanico de librerías que ofrece para resolver problemas de forma ágil y fácil.

En este repositorio encontrarás ejemplos de implementaciones de los algoritmos más importantes y que como programador deberías saber. Este repositorio se encuentra basado en el libro ![**Grokking algorithms**](https://www.manning.com/books/grokking-algorithms-second-edition) de Aditya Y. Bhargava.

# Algoritmos
<img src="https://roa.cedia.edu.ec/webappscode/63/algoritmo.jpg" alt="descripción de algoritmos" width="280">

Son un conjunto de pasos o instrucciones detalladas para resolver un problema específico. Para comprender este significado, nuestro algoritmo será la receta que nos indicará como hacer un plato de comida, este detallará los ingredientes y los pasos a seguir para obtener el resultado deseado.

# Estructuras de datos
<img src="https://www.df.cl/noticias/site/artic/20210125/imag/foto_0000000220210125121821.jpg" alt="bodega con productos" width="280">
Son formas que permiten organizar los datos en tiempo de ejecución de nuestro programa. Estas estructuras nos permiten almacenar, organizar y manipular los datos de forma eficiente. Es por esto que tener una visión clara y saber el uso de cada una de las estructuras de datos, nos favorecerá cumplir con los requerimientos de nuestros programas.

# Big O Notation
Es una notación matemática que describe la eficiencia de un algoritmo. En otras palabras, nos permite comparar la eficiencia de dos algoritmos y saber cuál es el mejor para resolver un problema específico.

Dentro de esta notación tendrémos diferentes tipos de tiempo de ejecución, los cuales son:

- `O(1)`: Tiempo de ejecución constante.
- `O(log n)`: Tiempo de ejecución logarítmico.
- `O(n)`: Tiempo de ejecución lineal.
- `O(n log n)`: Tiempo de ejecución logarítmico lineal.
- `O(n^2)`: Tiempo de ejecución cuadrático.
- `O(2^n)`: Tiempo de ejecución exponencial.

<img src="https://cdn-media-1.freecodecamp.org/images/1*KfZYFUT2OKfjekJlCeYvuQ.jpeg" alt="grafica big o notation" width="320">

Para este caso, cada uno de estos tiempos de ejecución se verá reflejado en el tiempo que tarda un algoritmo en ejecutarse, por lo que es importante tener en cuenta el tiempo de ejecución de cada uno de los algoritmos que implementemos.


# Funcionamiento de la memoria en nuestro sistema
Antes de empezar a conocer sobre estructuras de datos y algoritmos, es importante conocer como funciona la memoria en nuestro sistema a la hora de almacenar datos. En este caso, la memoria de nuestro sistema se divide en dos partes:

- **Stack**: En esta parte de la memoria se almacenan las variables y las funciones que se están ejecutando en el momento. Esta parte de la memoria es muy rápida y se utiliza para almacenar datos temporales.

- **Heap**: En esta parte de la memoria se almacenan los objetos que se crean en tiempo de ejecución. Esta parte de la memoria es más lenta que el stack, pero nos permite almacenar una mayor cantidad de datos.

Entonces, cuando creamos una variable en Python, esta se almacena en el stack, pero si creamos un objeto, este se almacena en el heap pero su dirección estará almacenada en el stack.

# Estructuras de datos

Ya que conocemos algunos de los algoritmos más importantes y tenemos una comprensión general de como almacena nuestra computadora los datos de nuestro programa, es hora de conocer las estructuras de datos y lo más importante, saber cuándo utilizar cada una de ellas.


## Arrays y Linked List

Ambas estructuras le piden a tu computadora que les reserve un espacio en memoria.

### Listas o Arrays
Las listas son una de las estructuras de datos más utilizadas en Python y en la informática general, estas nos permiten almacenar un conjunto de elementos de forma ordenada en la memoria de nuestro sistema y de **forma continua  (una tras de otra) en memoria**. Las listas son mutables, es decir, podemos modificar su contenido una vez que han sido creadas.

El gran problema de esta estructura de datos, es que dependeremos de la cantidad de memoria que tengamos en nuestro sistema, con esto quiero decir, cada elemento se almacena continuamene en memoria o una tras otro (como se veráa en la imagen).
<img src="https://i0.wp.com/javachallengers.com/wp-content/uploads/2023/01/array.png?resize=500%2C350&ssl=1" alt="refencia de memoria" width="250">

Entonces, si queremos aagregar otro elemento, este se tendrá que almacenar en otra parte de la memoria, lo que nos llevará a tener que buscar en otra parte de la memoria para obtener el siguiente elemento. Este proceso nos genera un gran problema y ya que si estaremos almacenando continuamente datos dentro de un arreglo lista, este bajaráa el performance de nuestro programa y cómputo pero hay una forma de solucionarlo, la alternativa a este proceso es asignara un espacio en memoria al momento de declarar esta estructura de datos pero puede pasar lo mismo, que necesitemos más espacio en memoria para almacenar más datos.

### Linked List (Listas enlazadas)
Al igual que un arreglo, esta estructura de datos nos permite almacenar un conjunto de elementos de forma ordenada en memoria pero la gran característica es que almacena los elemento de forma **no contínua**, esto quiere decir, que los elementos se almacenaran en diferentes partes de la memoria de nuestro sistema o donde haya espacio disponible. Entonces, ¿Cómo accederemos a los datos de forma ordenada?, cada elemento tiene la dirección de memoria del elemento sucesor, por lo que al momento de acceder a un elemento, este nos dará la dirección de memoria del siguiente elemento.

<img src="https://www.sahinarslan.tech/static/dd6ba2ed60f26c0811ad5052b66ad121/82d6d/linkedlistmemoryallocation.jpg" alt="Diferencias entre linked list y array">

### Diferencias entre ambas estructuras de datos

- Las listas enlazadas son ideales para ir almacenando datos de forma dinámica, es decir, no sabemos cuántos elementos vamos a almacenar en nuestra estructura de datos pero no lo son para acceder de forma aletaria a los datos, ya que tendremos que recorrer toda la lista para obtener el elemento deseado.

- Si queremos añadir elementos en la mitad de nuestra estructura de datos nuevos elementos, la lista enlazada será la indicada porque una vez que tengamos la dirección de memoria del elemento deseado, podremos añadir un nuevo elemento en cualquier parte de la lista y no tendremos que buscar una nueva dirección en memoria donde se almacenen los datos de forma contínua, y esto sucede igual al momento de realizar eliminaciones de elementos.

- Los arreglos como dijimos, son bastante buenos a la hora de acceder a elementos de forma aleatoria, ya que almacenan los elementos de forma contínua en memoria y está optimizado para acceder a los elementos de forma rápida.


- También los arreglos utilizan un poco menos de memoria al almacenar los elementos, ya que no necesitamos almacenar la dirección de memoria del elemento sucesor, como lo hace la lista enlazada y es por esto que un arreglo es más utilizado en la mayoría de los casos.

**Podemos concluir que ambas estructuras de datos tienen sus ventajas y desventajas, por lo que es importante saber cuándo utilizar cada una de ellas e incluso podemos hacer uso de una estructura de datos híbrida, donde almacenamos un conjunto de listas enlazadas dentro de un arreglo.**
