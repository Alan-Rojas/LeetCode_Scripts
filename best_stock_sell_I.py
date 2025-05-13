def maxProfit(prices):
    max_profit = 0
    min_price = float("inf")

    for i in prices:

        if i < min_price:
            min_price = i
        else: 
            max_profit = max(max_profit, i - min_price)

    return max_profit