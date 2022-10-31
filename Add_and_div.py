# Write a Python program to do arithmetical operations addition and division.

print ("Addition and division of two numbers")
a = int(input("enter any first number = "))
print("second number should not be '0' ")
b = int(input("enter anther number = "))

print("\n Addition of",a,"and " ,b,"is ", a+b)

if b== 0:
    print("\nAny number divided by ",b," is not-defined or infinity")
else:
    print("\n Division of",a,"and " ,b,"is ", a/b)
