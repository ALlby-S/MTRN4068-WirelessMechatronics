################## Importing modules ###############
#Modules bring functionality, a Library is a 
#collection of packages and modules.


#This file can be utilised as a module by navigating to this folder (MTRN4068-WirelessMechtraonics) in the terminal, then type "import Wk2_fibo"


def fib(n):
    a,b = 0,1
    while(a < n):
        print(a, end= ' ')
        a,b = b, a+b
        print()


def fib2(n):
    result = []
    a,b = 0,1
    while a < n:
        result.append(a)
        a,b = b, a+b
    return result


#Custom written:
#Aim is to create a code that outputs:
# *
# * *
# * * *
# ...

def stars(n):
    if n <= 0:
        return 0
    else:
        line = "*"
        x = 0
        while x < n:
            print(line)
            line = line + " *"
            x += 1
        print()