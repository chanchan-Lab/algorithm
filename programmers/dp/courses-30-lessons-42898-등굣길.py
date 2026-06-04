from collections import deque as dq

class dp_go_school():
    def __init__(self, m, n, puddles):
        self.m = m
        self.n = n
        self.puddles = puddles


    def dp_right_down(self):
        graph = [[0 for _ in range(self.n)] for _ in range(self.m)]
        
        q = dq()
        q.append((1,1))

        visited = set()
        visited.add((1,1))

        dx = [0,-1] # down, right
        dy = [1,0]  # down, right

        while q:
            (a,b) = q.popleft()

            for i in range(2):
                nx = a + dx[i]
                ny = b + dy[i]

                if (nx, ny) not in visited and nx >=0 and nx <=self.n-1 and ny >=0 and ny<=self.m and [nx,ny] not in self.puddles:
                    print(nx, ny)
                    graph[nx][ny] = graph[nx][ny+1] + graph[nx+1][ny]

                    q.append((nx, ny))
                    visited.add((nx,ny))
    
        print(graph)



m = 4
n = 3
puddles = [[2,2]]
a=dp_go_school(m, n, puddles)

a.dp_right_down()

def solution(m, n, puddles):
    answer = 0
    return answer