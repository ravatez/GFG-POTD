class Solution:
    def findTriplet(self, arr):
        arr.sort()
        for i in reversed(range(len(arr))):
            target = arr[i]
            left , right = 0, i - 1
            
            while left < right:
                if arr[left] + arr[right] == target:
                    return True
                elif arr[left] + arr[right] > target:
                    right -= 1
                else:
                    left += 1
        
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3
# Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.findTriplet(arr)
        if (res):
            print("true")
        else:
            print("false")
        # print(res)
        print("~")
        t -= 1

# } Driver Code Ends