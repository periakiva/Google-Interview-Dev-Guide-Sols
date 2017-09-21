
class maxProfit:
    def __init__(self,sell,buy):
        self.sell = sell
        self.buy = buy
        self.x = 'hello'
    def buySell(self,prices):
        mintemp = prices[0]
        profit = 0
        for i in xrange(0,len(prices)):
            if prices[i] < mintemp:
                mintemp = prices[i]
            else:
                if prices[i] - mintemp > profit:
                    profit = prices[i] - mintemp

        return profit



a = maxProfit("sell","buy")
prices = [10000,210,32,450,1000,213]
print a.buySell(prices)
