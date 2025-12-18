from collections import deque

def array_challenge(arr, arr_length):
    st = deque()
    max_area = 0
    i = 0

    while i < arr_length:
        if not st or arr[st[-1]] <= arr[i]:
            st.append(i)
            i += 1
        else:
            top = st.pop()
            height = arr[top]
            width = i if not st else i - st[-1] - 1
            max_area = max(max_area, height * width)

    while st:
        top = st.pop()
        height = arr[top]
        width = i if not st else i - st[-1] - 1
        max_area = max(max_area, height * width)

    return max_area

print(array_challenge([2,1,3,4,1], 5))  # 6
