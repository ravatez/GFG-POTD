class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.

                #Your Code goes here.
        dic = {}
        n = len(arr)
        
        # Counting occurrences of each element
        for i in arr:
            dic[i] = dic.get(i, 0) + 1
        
        # Finding elements that appear more than n // 3 times
        ans = [i for i in dic if dic[i] > (n // 3)]
        
        ans.sort()  # Sorting the result
        return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.findMajority(nums)
        if not ans:
            print("[]")
        else:
            print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()

# } Driver Code Ends