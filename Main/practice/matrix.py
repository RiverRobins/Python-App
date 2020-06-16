def cubic(n):
    main = []
    i = 0
    while i < (n * n):
        main.append([])
        i += 1
    num = 1
    for ar in main:
        i = 0
        while i < n:
            ar.append(num)
            num += 1
            i += 1

    return main


print(cubic(3))