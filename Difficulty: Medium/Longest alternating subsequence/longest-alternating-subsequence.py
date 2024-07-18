#User function Template for python3
class Solution:
    # Function to find the maximum length of alternating subsequence
    def alternatingMaxLength(self, arr):
       #code here
        if not arr:  # If the array is empty
            return 0

        count = 1  # Start with the first element
        increasing = None  # We don't know if it's increasing or decreasing yet

        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                if increasing is not True:  # Change to increasing
                    count += 1
                    increasing = True
            elif arr[i] < arr[i - 1]:
                if increasing is not False:  # Change to decreasing
                    count += 1
                    increasing = False

        return count

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    tc = int(data[0])
    for i in range(1, tc + 1):
        s = data[i].strip().split()
        nums = list(map(int, s))
        obj = Solution()
        ans = obj.alternatingMaxLength(nums)
        print(ans)

# } Driver Code Ends