def main():
    n = int(input())
    a = list(map(int, input().split()))
    sports_man = {}
    for i in range(2 ** n):
        sports_man[a[i]] = i
    while len(a) > 2:
        b = []
        for i in range(0, 2 ** n, 2):
            b.append(max(a[i], a[i + 1]))
        a = b.copy()
        n -= 1

    print(sports_man[min(a[0], a[1])] + 1)


if __name__ == '__main__':
    main()
