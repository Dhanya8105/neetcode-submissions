class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=l+1#here l indicates the day to buy stocks and r indicates the day to sell; so l<r is preferred for profit
        #here you can also do l,r=0,1
        maxp=0
        while r < len(prices):
            if prices[l]<prices[r]:
                profit=prices[r]-prices[l]
                maxp=max(maxp,profit)
            else:
                l=r#if you find that r is smaller than l,...then it is better to buy stocks on that day itself
            r+=1#to keep the loop running
        return maxp