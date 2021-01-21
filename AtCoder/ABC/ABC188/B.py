def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    norm = 0
    for i in range(n):
        norm += a[i] * b[i]
    if norm == 0:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
