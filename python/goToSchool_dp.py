def solution(m, n, puddles):
    matrix = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    MOD = 1_000_000_007
    matrix[n - 1][m - 1] = 1
    
    for i in range (n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if [j+1, i+1] not in puddles:
                matrix[i][j] = (matrix[i][j] + matrix[i+1][j] + matrix[i][j+1]) % MOD
            else :
                matrix[i][j] = 0
                
    return matrix[0][0]

print(solution(4, 3, [[2,2]]))