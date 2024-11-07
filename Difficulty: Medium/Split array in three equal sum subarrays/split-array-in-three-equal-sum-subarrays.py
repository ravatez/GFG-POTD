#User function Template for python3
class Solution:
    
    def findSplit(self, arr):
        # Return an array of possible answer, driver code will judge and return true or false based on
        total_sum = sum(arr)
        
        # Check if total_sum is divisible by 3
        if total_sum % 3 != 0:
            return [-1, -1]
        
        target_sum = total_sum // 3
        current_sum = 0
        first_split = -1
        second_split = -1
        
        for i in range(len(arr)):
            current_sum += arr[i]
            
            # Check for the first split point
            if current_sum == target_sum and first_split == -1:
                first_split = i
            
            # Check for the second split point after the first split
            elif current_sum == 2 * target_sum and first_split != -1:
                second_split = i
                break
        
        if first_split != -1 and second_split != -1:
            return [first_split, second_split]
        
        return [-1, -1]


#{ 
 # Driver Code Starts
# Initial Template for Python 3

# Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        arr = [int(x) for x in input().strip().split()]

        ob = Solution()
        result = ob.findSplit(arr)

        if (result == [-1, -1]) or len(result) != 2:
            print("false")
        else:
            sum1 = sum2 = sum3 = 0
            for i in range(len(arr)):
                if i <= result[0]:
                    sum1 += arr[i]
                elif i <= result[1]:
                    sum2 += arr[i]
                else:
                    sum3 += arr[i]

            if sum1 == sum2 == sum3:
                print("true")
            else:
                print("false")
        print("~")

# } Driver Code Ends