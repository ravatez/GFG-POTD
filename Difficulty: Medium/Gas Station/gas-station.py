class Solution:
    def startStation(self, gas, cost):
        # Your code here
        # First, check if there's enough total gas to complete the circuit
        if sum(gas) < sum(cost):
            return -1
        
        # If total gas is sufficient, there must be a valid starting point
        start_index = 0
        current_gas = 0
        
        for i in range(len(gas)):
            # Update current gas level after visiting station i
            current_gas += gas[i] - cost[i]
            
            # If we can't reach the next station
            if current_gas < 0:
                # Try starting from the next station
                start_index = i + 1
                # Reset the gas tank
                current_gas = 0
        
        # If we've gone through all stations and total gas >= total cost,
        # then the start_index must be valid
        return start_index


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        gas = list(map(int, input().strip().split()))
        cost = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.startStation(gas, cost)
        print(ans)
        print("~")

# } Driver Code Ends