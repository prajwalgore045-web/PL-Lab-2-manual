a = int(input("enter value: "))
count = 0

while a != 0:
    a = a // 10
    count += 1

print(count, "digits present")