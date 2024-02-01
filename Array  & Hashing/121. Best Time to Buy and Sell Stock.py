def maxProfit( prices: list[int]) -> int:
    buy = prices[0]
    res = 0
    for price in prices:
        if price > buy:
            res = max(res, price - buy)
        else:
            # means buying price is not lowest
            buy = price
        
    return res


prices = [2,1,2,1,0,1,2]
print(maxProfit(prices))