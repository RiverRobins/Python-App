def coinChange(coins, amount: int) -> int:
    coins.sort(reverse=True)
    count = 0
    temp = 0
    changed = True
    while temp < amount:
        if changed:
            for coin in coins:
                if coin + temp <= amount:
                    temp += coin
                    count += 1
                    break
                elif coin + temp > amount:
                    if coins.index(coin) == len(coins) - 1:
                        changed = False
                        break
                    else:
                        continue
                if temp == amount:
                    changed = False
                    break
        else:
            break
    if temp == amount:
        return count
    else:
        return -1


print(coinChange([1, 2, 5], 11))
print(coinChange([4, 6, 12], 19))
print(coinChange([1, 9, 4], 11))
print(coinChange([2, 3, 5], 100))