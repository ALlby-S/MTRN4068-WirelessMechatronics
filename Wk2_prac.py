#1. print hello world

##### Functions need to be defined above the code that uses the function.
def hello():
    #Triple quotes are used as Comments
    """Print "Hellow World" and Return None."""
    print("\n Hello World")

for _ in range(5):
    hello()

print("\n")


#2. printing something else
a = 1
if a == 2:
    print("a equals 2. \n")


#3. FLoat numbers
fnum = 5.0
print(fnum)
fnum2 = float(20) #Type casting.
print(fnum2)

#4. Defning strings
##In Pyhton strings can be defined with single or double quotes
name1 = "What's going on m8"
name2 = 'What in the world is going on??'
print(name1 +' '+ name2) #strings can be appended together!
print("\n")


#5. Defning several variables in one line
a,b,c = 1,2,3

print("a = " + str(a)) #Casting an int as a string
print("b = " + str(b))
print("c = " + str(c))

