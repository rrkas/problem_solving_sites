T = int(input())
for _ in range(T):
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))
    new_s = sum(arr)
    # print(new_s)
    e_c = {e: arr.count(e) for e in set(arr)}
    # print(e_c)
    config = None
    for k, v in e_c.items():
        for i in range(v + 1):
            t_s = new_s - 2 * (i * k)
            if t_s == s:
                config = (k, v, i, t_s)
                break

        if config:
            break

    if config:
        print("YES")
        # print(config)
        print(config[0])
    else:
        print("NO")
