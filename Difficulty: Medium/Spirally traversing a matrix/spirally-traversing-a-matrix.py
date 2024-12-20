class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, mat):
        # code here
        # code here
        ans,l,r,u,d=[],0,len(mat[0])-1,0,len(mat)-1
        while l<=r and u<=d:
            for i in range(l,r+1): ans.append(mat[u][i])
            u+=1
            for i in range(u,d+1): ans.append(mat[i][r])
            r-=1
            if(u<=d):
                for i in range(r,l-1,-1): ans.append(mat[d][i])
                d-=1
            if(l<=r):
                for i in range(d,u-1,-1): ans.append(mat[i][l])
                l+=1
        return ans

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    for _ in range(t):
        r = int(data[index])
        c = int(data[index + 1])
        index += 2
        matrix = []
        for i in range(r):
            row = list(map(int, data[index:index + c]))
            matrix.append(row)
            index += c

        solution = Solution()
        result = solution.spirallyTraverse(matrix)
        print(" ".join(map(str, result)))
        print("~")

# } Driver Code Ends