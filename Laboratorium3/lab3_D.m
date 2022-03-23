%zadanie D

density = 10;
indeks = 184531;
times=[];
NArr = [500 1000 3000 6000 12000];
for N = NArr
    [Edges] = generate_network(N, density);

    d= 0.85;
    
    I=speye(N);
    B = sparse(Edges(2,:), Edges(1,:), 1, N, N);
    
    L=sum(B).';
    
    b=sparse(N,1);
    b(:,:) = (1-d)/N;
    
    A=spdiags(1./L,0,N,N);

    
    M = I - d*B*A;
    tic;
    r = M\b;
    times(end+1) = toc;
end

plot(NArr, times);
xlabel("Liczba stron - N");
ylabel("Czas rozwiązania układu równań liniowych [s]");
title("Zależność czasu rozwiązywanaia układu od liczby stron w sieci");
grid on;

saveas(gcf, "zadD_184531.png");