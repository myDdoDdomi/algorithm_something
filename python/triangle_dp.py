def solution(triangle):
    
    N = len(triangle)
    
    temp_list = [[] for _ in range(N-1)]
    
    
    for i in range(N - 2, -1, -1):
        for j in range(len(triangle[i])):
            temp = max(triangle[i+1][j], triangle[i+1][j+1])
            triangle[i][j] += temp
            
            
    return triangle[0][0]


solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])