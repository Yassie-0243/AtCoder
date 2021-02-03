def main():
    n = int(input())
    while n % 2 == 0:
        n //= 2
    sq = int(n ** 0.5)
    ans = sum(n % i == 0 for i in range(1, sq + 1)) * 2 - (sq * sq == n)
    print(ans * 2)


if __name__ == '__main__':
    main()