
class Solution:
    def countNumberswith4(self, n : int) -> int:
        # code here
        no = 0
        for i in range(n+1):
            if "4" in str(i):
                no += 1
        return no



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        obj = Solution()
        res = obj.countNumberswith4(n)

        print(res)

# } Driver Code Ends