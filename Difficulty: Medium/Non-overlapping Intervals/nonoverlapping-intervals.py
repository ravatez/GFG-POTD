#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def minRemoval(self, intervals):
        # Code here
        # Code here
        intervals.sort(key=lambda x: x[1])

        # Initialize variables
        end = float('-inf')
        count = 0
    
        # Iterate through the intervals
        for start, finish in intervals:
            if start < end:
                # There's an overlap; increment the count
                count += 1
            else:
                # No overlap; update the end time
                end = finish
    
        return count

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        intervals = [list(map(int, input().split())) for i in range(N)]
        ob = Solution()
        res = ob.minRemoval(intervals)
        print(res)
        print("~")
# } Driver Code Ends