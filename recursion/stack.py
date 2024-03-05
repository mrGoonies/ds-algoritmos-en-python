
# Llamamos otras funciones
def greet(name):
    print("Hello {}".format(name))
    
    # Agregamos esta función al Stack del OS hasta que termine de ejecutarse.
    greet2(name)
    print("Getting ready to say bye..")

    # Agregamos esta función al stack hasta que termine de ejecutarse.
    bye()

def greet2(name):
    print("How are you {}?".format(name))

def bye():
    print("Ok bye!")


# Creando un Call Stack recursivo
def fact(x):
    if x == 1:
        return 1
    else:
        #print(x)
        return x * fact(x-1)

if __name__ == "__main__":
    # Agregamos el primer proceso al stack de nuestro SO hasta que termine de ejecutarse
    greet("Maggie")
    print(fact(5))
    # Todas las funciones llamadas van a un Call Stack
