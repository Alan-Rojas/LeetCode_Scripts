def maxProfit(array):
    """
    Ok, let's think this trough... I am given an array of prices, and I need to find the best combination of sales to max profit. Since I can buy and sell whenever I want, I can just greedy search profits. 
    """
    max_profit = 0

    for i in range(1, len(array)):

        if array[i-1] < array[i]:
        
            max_profit += array[i] - array[i-1]


    return max_profit

