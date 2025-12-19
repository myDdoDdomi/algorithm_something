import heapq
from collections import defaultdict

def solution(operations):
    min_h = []
    max_h = []
    cnt = defaultdict(int)
    
    size = 0
    
    def clean_min():
        while min_h and cnt[min_h[0]] == 0:
            heapq.heappop(min_h)
            
    def clean_max():
        while max_h and cnt[-max_h[0]] == 0:
            heapq.heappop(max_h)
            
    for op in operations:
        cmd, x = op.split()
        x = int(x)
        
        if cmd == "I":
            heapq.heappush(min_h, x)
            heapq.heappush(max_h, -x)
            cnt[x] += 1
            size += 1
        else :
            if size == 0:
                continue
            
            if x == 1:
                clean_max()
                v = -heapq.heappop(max_h)
                cnt[v] -= 1
                size -= 1
            else :
                clean_min()
                v = heapq.heappop(min_h)
                cnt[v] -= 1
                size -= 1
                
    if size == 0:
        return [0, 0]
    
    clean_max()
    clean_min()
    return [-max_h[0], min_h[0]]

h = []
heapq.heappush(h, 5)
heapq.heappush(h, 2)
heapq.heappush(h, 3)
heapq.heappush(h, 7)

print(h[0])