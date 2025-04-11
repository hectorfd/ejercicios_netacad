def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)

introduction("Skywalker", "Luke")
introduction("Quick", "Jesse")
introduction("Kent", "Clark")

def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

adding(1, 2, 3)

def happy_new_year(wishes = True):
    print("Tres...")
    print("Dos...")
    print("Uno...")
    if not wishes:
        return

    print("¡Feliz año nuevo!")

happy_new_year()


def boring_function():
    return 123

x = boring_function()

print("La función boring_function ha devuelto su resultado. Es:", x)

value = None
if value is None:
    print("Lo siento, no contienes ningún valor")


def strange_function(n):
    if(n % 2 == 0):
        return True



print(strange_function(4))


def list_sum(lst):
    s = 0

    for elem in lst:
        s += elem

    return s

print(list_sum([5, 4, 3]))

def strange_list_fun(n):
    strange_list = []
    
    for i in range(n):
        strange_list.insert(-1,i)
    
    return strange_list

print(strange_list_fun(5))