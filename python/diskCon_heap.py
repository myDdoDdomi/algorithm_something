import heapq
from collections import deque

def solution(jobs):
    jobs.sort()
    n = len(jobs)
    
    hq = []
    time = 0
    idx = 0
    while idx < n or hq:
        while idx < n and jobs[idx][0] <= time:
            start, dur = jobs[idx]
            heapq.heappush()
            idx += 1
            
        if hq:
            dur, start = heapq.heappop(hq)
            time += dur
            total += time - start
        else :
            time = jobs[idx][0]
            
    return total // n


solution([[0, 3], [1, 9], [3, 5]])
