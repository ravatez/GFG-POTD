#User function Template for python3
import heapq
class Solution:
    def minCost(self, houses):
        n=len(houses)
        visited=set()
        minHeap=[(0,0)]
        totalCost=0
        
        while len(visited)<n:
            cost,curr=heapq.heappop(minHeap)
            if curr in visited:
                continue
            
            totalCost+=cost
            visited.add(curr)
            
            for nextHouse in range(n):
                if nextHouse not in visited:
                    dist=abs(houses[curr][0]-houses[nextHouse][0])+abs(houses[curr][1]-houses[nextHouse][1])
                    heapq.heappush(minHeap,(dist,nextHouse))
                    
        return totalCost




#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        edges = []

        for _ in range(n):
            temp = list(map(int, input().split()))
            edges.append(temp)

        obj = Solution()
        print(obj.minCost(edges))
        print("~")
# } Driver Code Ends