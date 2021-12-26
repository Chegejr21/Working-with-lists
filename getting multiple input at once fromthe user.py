
print("I am x\nand am the greatest\nthe eath will ever produce\nI am Chege jr......")
a = 5
print("the value of a is", a)
b = 5
if 20 > 10:
    print("The value of b is:", b)
input1 = input("Enter the value of a: ")
print(input1 * 10)

num1 = int(input("Enter a number: "))
print(num1)
name1 = input("Enter your name:")
print(name1)

print(type(num1))
print(type(name1))

x, y, z = input("Enter three two digit values: ").split()
print("the value of x is : ", x)
print("the value of y is : ", y)
print("the value of z is: ", z)
print("the first number is  {} and the second number is {} while the third number is {}".format(x, y, z))

c, d, e = [int(x) for x in input("Enter the values: ").split()]
print("the value of x is : ", c)
print("the value of x is : ", d)
print("the value of x is : ", e)
print("the first number is  {} and the second number is {} while the third number is {}".format(c, d, e))

c, d, e = [str(x) for x in input("Enter three names: ").split()]
print("the first name is  {} and the second name is {} while the third name is {}".format(c, d, e))


