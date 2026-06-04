# https://school.programmers.co.kr/learn/courses/30/lessons/12978
# 다익스트라

from collections import deque as dq


class Mael():

    def __init__(self, N, road, K):

        self.N = N # 마을 수 (노드수)
        self.road = road # 간선정보 (연결, 가중치)
        self.K = K # 시감

        self.graph = dict() # 연결리스트
        for i in range(N+1):
            self.graph[i] = []
            for r in self.road:
                if r[0]==i:
                    self.graph[i].append((r[1],r[2]))
                if r[1]==i:
                    self.graph[i].append((r[0],r[2]))

        # print(self.graph)

    def Dijkstra(self) :
        N = self.N
        K = self.K
        graph = self.graph
        
        INF = int(1e9) # 최대로 초기화

        q = dq()
        q.append(1)

        # 거리 테이블 (1에서부터 가는데 간선의 합의 최소만)
        distance = [INF for _ in range(N+1)]
        distance[1] = 0 

        while(q):
            now = q.popleft() # 현재 노드번호

            for (node, cost) in graph[now]:
                # print(now, node, cost)
                new_cost = distance[now] + cost 

                if new_cost<distance[node]: # q 갱신조건
                    distance[node] = min(new_cost, distance[node])
                    q.append(node)
            
                # print('q:', q)
                # print('distance:', distance)

            # print('--'*10)

        answer = 0
        for i in distance:
            if K >= i: 
                answer +=1

        print('>> answer: ', answer)
        return answer                        
            

def solution(N, road, K):
    answer = Mael(N, road, K) # 객체선언
    return answer.Dijkstra()

# main
if __name__ == "__main__":
    test = Mael(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3)
    test.Dijkstra()

'''
* 다익스트라 알고리즘 : 가중치 계산 결과가 최소가 되는 경로에만! 
[풀이]
- 최소 가중치를 갱신해야하니, INF로 초기화해서 min값을 갱신해가면 된다. 
'''