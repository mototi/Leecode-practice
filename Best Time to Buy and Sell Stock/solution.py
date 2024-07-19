def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    
    lowest = prices[0]
    
    max_profit = 0
    
    for p in prices:
        if p < lowest:
            lowest = p
            
        profit = p - lowest 
        max_profit = profit if profit > max_profit else max_profit
    
    return max_profit 
            

print(maxProfit([7,1,5,3,6,4])) # 5
print(maxProfit([7,6,4,3,1])) # 0

