#User function Template for python3

class Solution:
    def sameOccurrence(self, arr, x, y):
        # code here
        ans = 0 # Num same occurence
        count_x = 0 # Counter of num x upto index i
        count_y = 0 # Counter of num y upto index i
       
        # Dict to count indices with specific (count_x-count_y)
        diff = {0:1} # Count 0 occurence before starting
        
        for i in range(len(arr)):
            # Update counters
            if arr[i] == x:
                count_x += 1
            if arr[i] == y:
                count_y += 1
            # Unpdate num same occurence
            ans += diff.get(count_x - count_y, 0)
            # Update Dict
            diff[count_x - count_y] = diff.get(count_x - count_y, 0) + 1
 
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        x = int(input().strip())
        y = int(input().strip())
        ob = Solution()
        ans = ob.sameOccurrence(arr, x, y)
        print(ans)
        tc -= 1

# } Driver Code Ends