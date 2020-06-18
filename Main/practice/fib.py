def fib(n):
    prev = 0
    curr = 1
    i = 0
    while i < n:
        # print(curr)
        temp = curr
        curr += prev
        prev = temp

        i += 1
    return prev


print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))
print(fib(7))

