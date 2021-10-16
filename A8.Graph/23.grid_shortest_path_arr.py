class Solution:
    def ta(self, arr, x, y, dist, dest, X, Y, visited):
        if (x, y) == dest:
            visited[(x, y)] = dist
            return
        if x >= 0 and y >= 0 and x < X and y < Y and arr[x][y] != 0 and (x, y) not in visited:
            visited[(x, y)] = dist
            self.ta(arr, x+1, y, dist+1, dest, X, Y, visited)
            self.ta(arr, x-1, y, dist+1, dest, X, Y, visited)
            self.ta(arr, x, y+1, dist+1, dest, X, Y, visited)
            self.ta(arr, x, y-1, dist+1, dest, X, Y, visited)
            return visited[dest]            
            
    def shortestDistance(self,N,M,A,X,Y):
        #code here
        x = self.ta(A, 0, 0, 0, (X, Y), N, M, {(X, Y): -1})
        print(x)
        return 0        
                
    def st(self, N, M, A, X, Y):
        rr = [-1, 1, 0, 0]
        cc = [0, 0, -1, 1]
        visited = set()
        visited.add((0, 0))
        dist = None
        q = [(0, 0, 0)]
        while q:
            rrr, ccc, dist = q.pop(0)
            if (rrr, ccc) == (X, Y):
                return dist
            for i in range(4):
                r = rrr + rr[i]
                c = ccc + cc[i]
                if r >= 0 and c >= 0 and r < N and c < M and A[r][c] == 1 and (r, c) not in visited:
                    visited.add((r, c))
                    q.append((r, c, dist + 1))
        return -1
                    

if __name__ == "__main__":
    # arr = [[1, 0, 0, 0],
    #        [1, 1, 0, 1],
    #        [0, 1, 0, 1]]
    n, m = list(map(int, input().split()))
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    x, y = list(map(int, input().split()))
    g = Solution()
    # # g.shortestDistance(3, 4, arr, 2, 3)
    # x = g.st(3, 4, arr, 2, 1)
    x = g.st(n, m, arr, x, y)
    print(x)