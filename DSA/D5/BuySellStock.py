'''
Problem: Buy and sell stocks to get maximum profit. You can only buy and sell once.
Approach: Keep track of the minimum price and calculate the profit at each step.
TC: O(n)
SC: O(1)

'''

class Solution:
    def stockBuySell(self, arr, n):
        mini=arr[0]
        profit=0
        for i in range(n):
            cost=arr[i]-mini
            profit=max(cost,profit)
            mini=min(mini,arr[i])
        return profit
    
sol=Solution()
print(sol.stockBuySell([7,1,5,3,6,4],6))