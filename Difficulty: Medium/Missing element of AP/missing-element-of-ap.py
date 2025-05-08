#User function Template for python3

class Solution:
    def findMissing(self, arr):
        # code here
        # expectation the first element is not the missing element
        num_elements = len(arr)
        if num_elements > 2:
            if arr[1] - arr[0] < 0:
                progression = max(arr[1] - arr[0], arr[2]-arr[1])
            else:
                progression = min(arr[1] - arr[0], arr[2]-arr[1])
            begin = arr[0]
            expected_sum = int(((num_elements+1)/2) * (2*begin+(num_elements)*progression))
            total_sum = sum(arr)
            return expected_sum - total_sum
        elif num_elements == 2:
            return arr[1] + (arr[1]-arr[0])

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import sys
import math


def main():
    input = sys.stdin.read
    data = input().strip().split('\n')

    t = int(data[0])
    solution = Solution()

    for i in range(1, t + 1):
        arr = list(map(int, data[i].split()))
        print(solution.findMissing(arr))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends