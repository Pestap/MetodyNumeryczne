d=0.85;
N=7;

I=speye(N)

w1=sparse([4 6 3 4 5 5 6 7 5 6 4 6 4 7 6])
w2=sparse([1 1 2 2 2 3 3 3 4 4 5 5 6 6 7])
w3=sparse([1 1 1 1 1 1 1 1 1 1 1 1 1 1 1])

B=sparse(w1,w2,w3,N,N)

L=sum(B).' %L to wektor sum wierszy

b=sparse(N,1)
b(:,:) = (1-d)/N

A=spdiags(1./L,0,N,N)

M = I - d*B*A
r = sparse(M\b)

bar(r)