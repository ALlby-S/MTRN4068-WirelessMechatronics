#This application will accept 2 numbers from the user and output the multiplication result
def prod(a,b):
    result = a * b
    print(result)
    if result < 100:
        return a-b
    else:
        return result

num1 = float(input("Enter first number "))
num2 = float(input("Enter second number "))

res = num1 * num2
print(res)
