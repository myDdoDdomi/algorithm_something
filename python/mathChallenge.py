dic = ['+', '-']

def math_challenge(num):
    num_list = [int(i) for i in num]
    n = len(num_list)

    max_count = -1
    result = ""

    def dfs(idx, minus_count, total, now):
        nonlocal max_count, result
        if idx == n:
            if total == 0 and minus_count > max_count:
                max_count = minus_count
                result = now
            return

        dfs(idx + 1, minus_count, total + num_list[idx], now + '+')
        dfs(idx + 1, minus_count + 1, total - num_list[idx], now + '-')

    dfs(1, 0, num_list[0], "")
    return result if result else "not possible"

num = input().strip()
print(math_challenge(num))
