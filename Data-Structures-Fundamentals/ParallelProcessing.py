#Python3
import heapq
def scheduling(jobs, threads):
    result = []
    next_free_time = [[0,x] for x in range(0,threads)]
    for job in jobs:
        next = heapq.heappop(next_free_time)
        
        
        result.append([next[1],next[0]])
       
        next[0] += job
        heapq.heappush(next_free_time,next)
    return(result)

threads = [int(x) for x in input().split()]
jobs =  [int(x) for x in input().split()]
j = scheduling(jobs, threads[0])
for x in j:
    print(*x)