def fib(n):
    prev = 0
    curr = 1
    i = 0
    while i < n:
        print(curr)
        temp = curr
        curr += prev
        prev = temp

        i += 1


fib(10)
