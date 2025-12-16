from collections import defaultdict

def array_challenge(st):

    result = 0
    
    tempMap = defaultdict(set) # "aa aa odg gdo"
    
    for s in st :
        temp = "".join(sorted(s))
        tempMap[temp].add(s) # set이여서 add
    
    for key in tempMap :
        N = len(tempMap[key])
        
        if N <= 1 :
            continue
        
        result += (N - 1)
        
    print(result)
        
st_list = input().strip().split()

array_challenge(st_list)


