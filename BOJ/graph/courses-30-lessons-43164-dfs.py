from collections import deque as dq

# https://school.programmers.co.kr/learn/courses/30/lessons/43164
# 여행경로 - BFS

# tickets	return
# [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]	["ICN", "JFK", "HND", "IAD"]
# [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]	["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]

# ICN에서 시작해서 도착하는 곳까지.

class From_INC():
    def __init__(self, tickets):
        self.tickets = tickets

        graph = dict()
        for ticket in tickets:
            if ticket[0] not in graph:
                graph[ticket[0]] = []

            graph[ticket[0]].append(ticket[1])

        print('grpah:', graph)
        self.graph = graph

    # def bfs(self):
    #     tickets = self.tickets
    #     graph = self.graph

    #     q = dq()
    #     q.append("ICN")
    #     visited = set()
    #     visited.add("ICN")

    #     check 
        
    #     while(q):
    #         now = q.popleft()
            
    #         if now not in graph:
    #             print(q)
    #             break

    #         for next in graph[now]:
    #             if next not in visited:
    #                 q.append(next)
    #                 visited.add(next)
    #                 # if len(q) == len(tickets)+1:
    #                 #     print(q)

    def dfs(self):
        tickets = self.tickets
        graph = self.graph

        q = dq()
        q.append("ICN")
        visited = set()
        visited.add("ICN")

        return 0


                
test=From_INC([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
print(test.bfs())
    
'''

[풀이]
"만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다." >> 킥

가능한 경로가 2개 이상인 경우.
* (주의) 도착하는 곳은 출발지에 존재하지 않음. 
* 이건 끝까지 한번 찍고, 다시 뱉고 (반복) =>> DFS+백트래킹


'''




