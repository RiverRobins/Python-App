def coinChange(coins, amount: int) -> int:
    coins.sort(reverse=True)   #Ensures that array is sorted from greatest to least
    count = 0    #The amount of coins used
    temp = 0    #The collective value of all the coins currently being used
    changed = True   #Determines if array was affected by the loop
    while temp < amount:
        if changed:
            for coin in coins:
                if coin + temp <= amount: #If it can add the coin of the current iteration without going over the amount, it will do so and continue
                    temp += coin
                    count += 1
                    break
                elif coin + temp > amount: #If adding the current coin goes over the limit, move to the next smallest coin. If every coin goes over the limit, break the loop
                    if coins.index(coin) == len(coins) - 1:
                        changed = False
                        break
                    else:
                        continue
                if temp == amount: #If the value of the coins in use is the desired amount, break the loop
                    changed = False
                    break
        else:
            break
    if temp == amount: #if the collective value of coins is the desired amount, return amount of coins used. Else return -1
        return count
    else:
        return -1


print(coinChange([1, 2, 5], 11))
print(coinChange([4, 6, 12], 19))
print(coinChange([1, 9, 4], 11))
print(coinChange([2, 3, 5], 100))
