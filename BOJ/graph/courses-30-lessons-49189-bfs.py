# https://school.programmers.co.kr/learn/courses/30/lessons/49189 문제
# 유형: 양방향 BFS 

# n = 6
# edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

'''
[작전]
인접리스트 -> 거리배열 완성 

'''
from collections import deque

class Graph_List:
    def __init__(self, n, edge):
        self.n = n
        self.edge = edge

        self.grap = {}

        for i in range(n+1):
            self.grap[i] = []

        for num in edge : 
            self.grap[num[0]].append(num[1])
            self.grap[num[1]].append(num[0])

        print(self.grap) # {0: [], 1: [3, 2], 2: [3, 1, 4, 5], 3: [6, 4, 2, 1], 4: [3, 2], 5: [2], 6: [3]}

# 2. 1번에서 얼마나 떨어졌는지  배열로 저장

    def bfs(self):

        n = self.n
        grap = self.grap

        q = deque()
        q.append(1)

        visited = set()
        visited.add(1)

        dist_from_1 = [0 for i in range(n+1)] #[0,0,0,...,0]

        while q:
            now = q.popleft()

            for next in grap[now]:
                if next not in visited and next<=n and next>0:
                    dist_from_1[next] = dist_from_1[now] + 1
                    q.append(next)
                    visited.add(next)

                    print('q: ', q)
                    print('visited: ', visited)

        print('dist_from_1 최종 :', dist_from_1)

        answer = dist_from_1.count(max(dist_from_1))
        return answer

class Graph_metrix():
    def __init__(self, n, edge):
        self.n = n
        self.edge = edge
        
        metrix = [[0 for _ in range(n+1)] for _ in range(n+1)]
        self.metrix = metrix

        for i,j in edge:
            metrix[i][j]=1
            metrix[j][i]=1
        
        print(metrix)

    def bfs(self):
        n = self.n
        edge = self.edge
        graph = self.metrix
        
        q = deque()
        q.append(1)

        visited = set()
        visited.add(1)

        dist_from_1 = [0 for i in range(n+1)] #[0,0,0,...,0]

        while q:
            now = q.popleft() #node


            for next in range(1,n+1):
            
                if graph[now][next]==1 and next not in visited: # q갱신조건
                    dist_from_1[next] = dist_from_1[now] + 1
                    q.append(next)
                    visited.add(next)

                    print('q: ', q)
                    print('visited: ', visited)

        print('dist_from_1 최종 :', dist_from_1)

        answer = dist_from_1.count(max(dist_from_1))
        return answer
        
def solution(n , edge):
    # g = Graph_List(n,edge)
    g = Graph_metrix(n,edge)
    return g.bfs()


# main
if __name__ == "__main__":
    n = 6
    edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
    
    
    print('>> answer:', solution(n, edge))



'''
* Graph_List의 경우, 노드수가 상대적으로 많고, 간선수가 상대적으로 적을때 유리하다.
* Graph_metrix의 경우, 노드수가 상대적으로 적고!!, 연결상태를 빠르게 확인하고싶을때 유리하다. (노드수x노드수 배열이니..)


'''