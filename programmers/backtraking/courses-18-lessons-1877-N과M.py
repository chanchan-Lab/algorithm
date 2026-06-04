# https://school.programmers.co.kr/learn/courses/18/lessons/1877
# 백트래킹 [교과서-순열/조합/중복순열/중복조합] 
# [Permutation/Combination/Permutation with Repetition/Combination with Repetition]

class Combinatorics(): # 조 합 론
    def __init__(self, n, m):
        self.n = n
        self.m = m
        

    def dfs_Permutation(self, start, buf):
        n = self.n
        m = self.m

        # 종료조건
        if len(buf) == self.m:
            print('--- dfs 끝 ----')
            print(buf)
            return

        for i in range(start, n+1):
            
            # 중복검사
            if i not in buf:
                buf.append(i)
            
                print(buf)

                self.dfs_Permutation(start, buf)

                buf.pop()
                print(buf)
        
test_C = Combinatorics(5,2)
print(test_C.dfs_Permutation(3,[]))
        

