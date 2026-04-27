a=int(input("enter value: "))
b=int(input("enter value: "))
print("using temp: ")
temp=a
a=b
b=temp
print(f"value of a is {a} and value of b is {b}")
print("without temp")
a=int(input("enter value: "))
b=int(input("enter value: "))
a=a+b
b=a-b
a=a-b
print(f"value of a is {a} and value of b is {b}")