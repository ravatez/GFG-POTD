class Solution:
    def canSplit(self, arr):
        #code here
        l = 0
        r = len(arr) - 1
        sm1 = arr[l]
        sm2 = arr[r]
        while l < r:
            if sm1 == sm2:
                l += 1
                if l >= r:
                    return sm1 == sm2
                r -= 1
                sm1 += arr[l]
                sm2 += arr[r]
            elif sm1 < sm2:
                l += 1
                sm1 += arr[l]
            else:
                r -= 1
                sm2 += arr[r]
 
        return False
        

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0])
    index = 1
    for _ in range(t):
        arr = list(map(int, data[index].split()))
        index += 1

        obj = Solution()
        res = obj.canSplit(arr)
        if (res):
            print("true")
        else:
            print("false")

# } Driver Code Ends