%zadanie A

N = 10;
density = 3;
indeks = 184531;

[Edges] = generate_network(N, density);


%zadanie B
N =10;
d= 0.85;

I=speye(N);
B = sparse(Edges(2,:), Edges(1,:), 1, N, N);

L=sum(B).';

b=sparse(N,1);
b(:,:) = (1-d)/N;

A=spdiags(1./L,0,N,N);

save zadB_184531 A B I b

%zadanie C

M = I - d*B*A;
r = M\b;

save zadC_184531 r;
