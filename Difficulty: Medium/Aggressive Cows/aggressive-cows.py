#User function Template for python3


class Solution:

    def aggressiveCows(self, stalls, k):
        # Step 1: Sort the stall positions
        stalls.sort()
        
        # Step 2: Initialize binary search boundaries
        start = 1  # Minimum possible distance
        end = stalls[-1] - stalls[0]  # Maximum possible distance
        
        ans = 0  # Variable to store the largest minimum distance
        
        # Step 3: Binary Search
        while start <= end:
            mid = start + (end - start) // 2  # Integer division
            
            # Try to place cows with a minimum distance of 'mid'
            cow_count = 1  # Place the first cow at stalls[0]
            prev_pos = stalls[0]
            
            for i in range(1, len(stalls)):
                if stalls[i] - prev_pos >= mid:  # Place the next cow
                    cow_count += 1
                    prev_pos = stalls[i]
                    
            # Step 4: Check if we can place all 'k' cows
            if cow_count >= k:
                ans = mid  # Update the answer
                start = mid + 1  # Search for a larger minimum distance
            else:
                end = mid - 1  # Reduce the search space
                
        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.aggressiveCows(A, D)
        print(ans)
        print("~")
# } Driver Code Ends