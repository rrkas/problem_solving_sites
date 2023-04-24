n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

for i in range(n):
    pref = arr1[: i + 1]
    suff = arr1[n - i - 1 :]
    # print(pref, suff)
    min_n = arr2[i]

    if len(pref) >= min_n:
        pref.sort()
        suff.sort()
        print(max(pref[min_n - 1], suff[min_n - 1]), end=" ")
    else:
        print(0, end=" ")
