#User function Template for python3
class Solution:
    def sumClosest(self, arr, target):
        # code here
        # code here
        arr.sort() 
        left = 0 # start at left 
        right = len(arr)-1 #start at right
        closest_sum = float('inf')
        closest_pair = []
        
        while left < right:
            current_sum = arr[left] + arr[right]
            
            if abs(target - current_sum) < abs(target - closest_sum):
                closest_sum = current_sum
                closest_pair = [arr[left],arr[right]]
                
            if current_sum < target:
                left += 1
                
            elif current_sum > target:
                right -= 1
                
            else:
                break
            
        return closest_pair


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    while t > 0:
        arr = list(map(int, input().strip().split()))
        target = int(input().strip())
        ob = Solution()
        ans = ob.sumClosest(arr, target)
        if not ans:
            print("[]")
        else:
            print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends