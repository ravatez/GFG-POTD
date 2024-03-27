#User function Template for python3

#User function Template for python3
class Union:
    def __init__(self,n):
        self.parent = [i for i in range(n+1)]
        self.rank = [1]*(n+1)
    def find(self,x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def nat(self,n):
        if n<0:
            return 0
        return (n*(n+1))//2
    def union(self,x,y):
        X = self.find(x)
        Y = self.find(y)
        # print(self.rank[X],self.rank[Y],X,Y)
        ans = self.rank[X]*self.rank[Y]
        if X!=Y:
            if self.rank[X]<self.rank[Y]:
                self.parent[X] = Y
                self.rank[Y]+=self.rank[X]
            else:
                # self.rank[X] = self.rank[Y]
                self.parent[Y] = X
                self.rank[X]+=self.rank[Y]
                # self.rank[Y]=self.rank[X]
        return ans
                
class Solution:
    def maximumWeight(self, n, edges, q, queries):
        edges.sort(key=lambda x:x[2])
        # print(edges)
        res = [0]*q
        pair  = []
        for i in range(len(queries)):
            pair.append([queries[i],i])
        pair.sort()
        i = 0
        j = 0
        prev = 0
        un = Union(n)
        while i<len(pair):
            count = prev
            while j<len(edges) and edges[j][2]<=pair[i][0]:
                x,y,w = edges[j]
                # print(x,y,w)
                xxx = un.union(x,y)
                # print(xxx)
                count+=xxx
                j+=1
            res[pair[i][1]] = count
            prev = count
            i+=1
        return res
        






#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())

        edges = [[0 for j in range(3)] for i in range(n-1)]
        for i in range(n-1):
            input_line = [int(x) for x in input().strip().split()]       
            for j in range (3):
                edges[i][j]=input_line[j]

        q = int(input())
        queries = list(map(int, input().strip().split()))

        ob = Solution()
        ans = ob.maximumWeight(n, edges, q, queries)
        for i in ans:
            print(i,end=" ")
        print()


# } Driver Code Ends