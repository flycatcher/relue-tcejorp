u(x) = sum(n = 0, 10, (-x)^n);
ans = sum(n = 1, 10, polinterpolate(vector(n, k, k), vector(n, k, u(k)), n + 1););
print(ans);
quit
