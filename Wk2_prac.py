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