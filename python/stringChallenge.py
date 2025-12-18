def string_challenge(str_arr, arr_length):
    
    if arr_length == 1 or arr_length >= len(str_arr) :
        return str_arr
        
    cur = 0
    dir = 1
    
    temp_list = ["" for _ in range(arr_length)]
    
    for s in str_arr :
        temp_list[cur] += s
        
        if cur == 0:
            dir = 1
        elif cur == arr_length - 1:
            dir = -1
            
        cur = cur + dir
    
    print(temp_list)
    #result = ""
    #print(temp_list)
    #for lis in temp_list:
    #    result += lis[0]
    
    result = "".join(temp_list)
        
    print(result)
    return result

str_arr = input()
arr_length = int(input())

print(string_challenge(str_arr, arr_length))