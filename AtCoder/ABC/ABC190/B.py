n, s, d = map(int, input().split())
ans = False
for _ in range(n):
    x_tmp, y_tmp = map(int, input().split())
    if x_tmp < s:
        if y_tmp > d:
            ans = True
            break

if ans:
    print('Yes')
else:
