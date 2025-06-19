# Problem 1672: Richest Customer Wealth
# Your solution:
class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        richestCustomerWealth = 0
        for i in range(len(accounts)):
            wealth = 0
            for j in range(len(accounts[i])):
                wealth += accounts[i][j]
            if wealth > richestCustomerWealth:
                richestCustomerWealth = wealth
            else:
                pass
        return richestCustomerWealth

