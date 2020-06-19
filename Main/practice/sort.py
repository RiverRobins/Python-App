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


# def linear(n):
#     temp = []
#     i = 0
#     while i < len(n):
#         i2 = 0
#         while i2 < len(temp):
#             if n[i] <= temp[i2]:
#                 temp.insert(n[i], i2)
#             i2 += 1
#         i += 1
#     return temp


nums = [10, 3, 1, 2, 4, 11, 8, 6, 7]

print(bubble(nums))
# print(linear(nums))
