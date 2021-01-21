def main():
    N, C = map(int, input().split())
    event = []
    for i in range(N):
        a_tmp, b_tmp, c_tmp = map(int, input().split())
        event.append((a_tmp - 1, c_tmp))
        event.append((b_tmp, -c_tmp))

    event.sort()
    ans = 0
    fee = 0
    t = 0
    for x, y in event:
        if x != t:
            ans += min(C, fee) * (x - t)
            t = x
        fee += y
    print(ans)


if __name__ == '__main__':
    main()
