class Solution:
	def mergeOverlap(self, arr):
		#Code here
        arr.sort()
        t = []
        
        l, r = arr[0][0],arr[0][1]
        
        for i in arr[1:]:
            if i[0] > r:
                t.append([l, r])
                l, r = i
            else:
                r = max(r, i[1])
        
        t.append([l, r])
        return t

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        # a = list(map(int, input().strip().split()))
        arr = []
        # j = 0
        for i in range(n):
            a = list(map(int, input().strip().split()))
            x = a[0]
            # j += 1
            y = a[1]
            # j += 1
            arr.append([x, y])
        obj = Solution()
        ans = obj.mergeOverlap(arr)
        for i in ans:
            for j in i:
                print(j, end=" ")
        print()

# } Driver Code Ends