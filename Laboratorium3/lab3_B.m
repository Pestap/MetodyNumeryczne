N =10;
d= 0.85;

I=speye(N);
B = sparse(Edges(2,:), Edges(1,:), 1, N, N);

L=sum(B).';

b=sparse(N,1);
b(:,:) = (1-d)/N;

A=spdiags(1./L,0,N,N);

save zadB_184531 A B I b