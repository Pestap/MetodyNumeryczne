clc
clear

N = 931;
e = ones(N, 1);

M = spdiags([-e -e 10*e -e -e], -2:2,N,N);

D = diag(diag(M));
D = full(D);
U = triu(M, 1);
L= tril(M, -1);
U = full(U);
L = full(L);
A = full(M);
D*(U+L);
v = 0:N-1;
V = sin(5 * v);

R = M\(V.')