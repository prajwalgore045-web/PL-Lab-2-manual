num = int(input())
sum = 0
temp = num

while temp:
    d = temp % 10
    sum += d**3
    temp //= 10

print("Armstrong" if sum == num else "Not Armstrong")