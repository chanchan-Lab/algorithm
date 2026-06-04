'''
5 5
#####
#..B#
#.#.#
#RO.#
#####

7 7
#######
#...RB#
#.#####
#.....#
#####.#
#O....#
#######

'''

N, M = map(int, input().split(' '))
graph = []
for i in range(N):
    graph.append(list(input()))

print(graph)