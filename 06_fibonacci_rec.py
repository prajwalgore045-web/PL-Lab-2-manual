def fib(n):return n if n<=1 else fib(n-1)+fib(n-2)
n=int(input());[print(fib(i),end=' ') for i in range(n)]