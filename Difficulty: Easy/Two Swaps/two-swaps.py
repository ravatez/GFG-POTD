class Solution:
    def find_idx(self,n,arr,ele):
        for i in range(n):
            if arr[i]==ele:
                return i
            
    def checkSorted(self, arr):
        count=0
        n=len(arr)
        for i in range(n):
            if arr[i]!=i+1:
                idx=self.find_idx(n,arr,i+1)
                arr[i],arr[idx]=arr[idx],arr[i]
                count+=1
                if count>2:
                    return False
        if count==0 or count==2:
            return True
        return False


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        arr = list(map(int, input().split()))

        sol = Solution()
        result = sol.checkSorted(arr)
        if result:
            print("true")
        else:
            print("false")

# } Driver Code Ends