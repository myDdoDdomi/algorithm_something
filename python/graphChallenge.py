from collections import defaultdict, deque

def graphChallenge(str_arr, arr_length) :
    
    N = int(str_arr[0])
    
    node_graph = defaultdict(list)
    
    node_names = str_arr[1: N + 1]
    
    for i in range (N + 1, arr_length):
        s, e = str_arr[i].split('-')
        node_graph[s].append(e)
        node_graph[e].append(s)
    
    start_node = node_names[0]
    end_node = node_names[-1]
    
    q = deque()
    q.append([start_node, start_node])
    
    visited = set()
    visited.add(start_node)
    
    result = ""
    
    while q :
        cur, path = q.popleft()
        
        if cur == end_node :
            result = path
            break
        
        for n in node_graph[cur]:
            if n not in visited :
                visited.add(n)
                q.append([n, path + "-" + n])
    
    # q.append({})
    
    print(node_graph)
    print(result)
    


graphChallenge(["5","A","B","C","D","F","A-B","A-C","B-C","C-D","D-F"] , 11)

# {"5","A","B","C","D","F","A-B","A-C","B-C","C-D","D-F"}