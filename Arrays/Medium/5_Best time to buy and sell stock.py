def best_stock(arr):

    min_price = arr[0]
    max_profit = 0

    for num in arr:

        min_price = min(min_price, num)
        profit = num - min_price
        max_profit = max(max_profit, profit)

    return max_profit
       

arr = [10, 7, 5, 8, 11, 9]
print(best_stock(arr))



