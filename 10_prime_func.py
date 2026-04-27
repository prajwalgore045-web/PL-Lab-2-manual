def p(n):return n>1 and all(n%i!=0 for i in range(2,n))
print('Prime' if p(int(input())) else 'Not Prime')