class Solution:
    def subarrayXor(self, arr, k):
        # code here
        freq={0:1}
        preXor=0
        ans=0
        for item in arr:
            preXor^=item
            ans+=freq.get(preXor^k,0)
            freq[preXor]=freq.get(preXor,0)+1
        return ans

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    tc = int(input())

    for _ in range(tc):
        arr = list(map(int, input().split()))
        k = int(input())

        obj = Solution()
        print(obj.subarrayXor(arr, k))
        print("~")

# } Driver Code Ends