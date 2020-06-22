def bubble(n):
    changed = True
    while changed:
        i = 0
        while i < len(n) - 1:
            if n[i] > n[i + 1]:
                temp = n[i]
                n[i] = n[i + 1]
                n[i + 1] = temp
                changed = True
                break
            else:
                changed = False
            i += 1
    return n


def linear(n):
    changed = True
    while changed:
        i = 0
        while i < len(n) - 1:
            if n[i] < n[0]:
                temp = n[i]

                i2 = 0
                next = 0
                prev = 0
                while i2 < len(n) - 1:
                    locals()
                    next = n[i2 + 1]
                    n[i2] = prev
                    i2 += 1

                n[0] = temp
                changed = True
                break
            else:
                changed = False
            i += 1
    return n


nums = [10, 3, 1, 2, 4, 11, 8, 6, 7]

print(bubble(nums))
# print(linear(nums))
