class Solution:
    def maximumProfit(self, prices):
        # code here
        # Initialize variables for minimum price and maximum profit
        min_price = float('inf')
        max_profit = 0

        # Iterate through the list of prices
        for price in prices:
            # Update the minimum price seen so far
            min_price = min(min_price, price)
            # Calculate potential profit and update max_profit
            max_profit = max(max_profit, price - min_price)

        return max_profit

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())  # Read number of test cases
    for _ in range(t):
        # Read input and split it into a list of integers
        prices = list(map(int, input().split()))
        # Create a Solution object and calculate the result
        obj = Solution()
        result = obj.maximumProfit(prices)
        # Print the result
        print(result)

# } Driver Code Ends