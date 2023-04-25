n, q = map(int, input().split())
arr = list(map(int, input().split()))

for e in range(q):
    parts = list(map(int, input().split()))
    if parts[0] == 1:
        idx = parts[1] - 1
        v = parts[2]
        arr[idx] = v
    else:
        parr = [arr[0]]
        for e in arr[1:]:
            parr.append(e + parr[-1])

        # print(parr)
        lidx = -1
        ridx = -1
        for i, le in enumerate(parr):
            if le > 0:
                if lidx == -1:
                    lidx = i
                if i > ridx:
                    ridx = i
        if lidx > -1 < ridx:
            print(lidx + 1, ridx + 1)
        else:
            print(-1)
