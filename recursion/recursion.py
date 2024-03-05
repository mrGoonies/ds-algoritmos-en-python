""" Implementando recursion en Python """

def infinite_loop(i):
    """ Creando una función recursiva 
    print(i)
    infinite_loop(i-1)


def implement_recursion(i):
    print(i)

    if i <= 0 :
        return 

    implement_recursion(i-1)



if __name__ == "__main__":
    #infinite_loop(3)
    implement_recursion(3)
