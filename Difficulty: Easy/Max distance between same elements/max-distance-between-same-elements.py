class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    def maxDistance(self, arr):
        # Code here        
        index_map = {}
        max_dist = 0
        for index, value in enumerate(arr):
            if value in index_map:
                distance = index - index_map[value]
                max_dist = max(max_dist, distance)
            else:
                index_map[value] = index
        return max_dist



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.maxDistance(arr))

# } Driver Code Ends