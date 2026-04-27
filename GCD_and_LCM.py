a = int(input("Enter first number: ").strip())
b = int(input("Enter second number: ").strip())

x, y = a, b

while y != 0:
    x, y = y, x % y

gcd = x
lcm = (a * b) // gcd

print("GCD:", gcd)
print("LCM:", lcm)