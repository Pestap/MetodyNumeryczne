%zadanie A

NArr = [500 1000 3000 6000 12000];
density = 10;
indeks = 184531;

numberOfIterations = [];
timesElapsed = [];
resNormsArr = [];

for N = NArr
    resNorms = [];
    iterations = [];
    [Edges] = generate_network(N, density);
    
    
    %zadanie B
    d= 0.85;
    
    I=speye(N);
    B = sparse(Edges(2,:), Edges(1,:), 1, N, N);
    
    L=sum(B).';
    
    b=sparse(N,1);
    b(:,:) = (1-d)/N;
    
    A=spdiags(1./L,0,N,N);
    M = I - d*B*A;
    
    
    %Jacobi - działa 
    
    D = diag(diag(M)); %tworzymy macierz złożoną tylko z elementów diagonali
    L = tril(M, -1); %macierz trójkątna dolna, bez diagonali
    U = triu(M, 1); %macierz trójkątna górna, bez diagonali
    
    %rnJ = M\b; % do porównania wyników
    
    rk = ones(N,1); % początkowa inicjalizacja wektora rk
    

    tic
    DLU = -D\(L+U); %obliczamy -D^-1(L+U), które występuje w każdej iteracji
    Db = D\b; % obliczamy czynnik D(-1) * b który jest stały w każdej iteracji
    
    counter = 0;
    
    while norm(M*rk - b) > 10^(-14) %sprawdzamy normee residuum
        resNorms(end +1 ) = norm(M*rk -b);
        iterations(end + 1) = counter;
        counter = counter + 1; % zwiększamy licznik
        rk = DLU*rk + Db;
    end
    timesElapsed(end + 1) = toc;
    numberOfIterations(end+1) = counter;
    if N == 1000
        figure('Name', "Norma wektora residuum");
        semilogy(iterations, resNorms);
        grid on
        title("Norma residuum w metodzie Jacobi'ego dla N = 1000");
        xlabel("Liczba iteracji");
        ylabel("Norma wektora residuum");
        saveas(gcf, "zadE_184531_3.png")
    end
end

figure('Name', "Liczba iteracji");
plot(NArr, numberOfIterations);
grid on;
title("Liczba iteracji a N w metodzie Jacobi'ego");
ylabel("Liczba iteracji");
xlabel("Liczba stron - N")
saveas(gcf, "zadE_184531_1.png");

figure('Name', "Czas obliczeń");
plot(NArr, timesElapsed);
grid on;
title("Czas obliczeń a N w metodzie Jacobi'ego");
ylabel("Czas obliczeń [s]")
xlabel("Liczba stron - N");
saveas(gcf, "zadE_184531_2.png");




