class Solution:
    def celebrity(self, mat):
        # code here
        n=len(mat)
        top=0
        bot=n-1
        while top<bot:
            if mat[top][bot]:
                top+=1
            else:
                bot-=1
        for i in range(n):
            if i!=top and (mat[top][i] or mat[i][top]==0):
                return -1
        return top

#{ 
 # Driver Code Starts
# Main function to handle input and output
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        M = []
        for _ in range(n):
            M.append(list(map(int, input().split())))

        ob = Solution()
        print(ob.celebrity(M))

# } Driver Code Ends