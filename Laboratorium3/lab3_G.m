load Dane_Filtr_Dielektryczny_lab3_MN.mat

%wbudowana metoda
tic;
r = M\b;
defaultTime = toc;

N = size(M,1);

%Jacobi
tic
D = diag(diag(M)); %tworzymy macierz złożoną tylko z elementów diagonali
L = tril(M, -1); %macierz trójkątna dolna, bez diagonali
U = triu(M, 1); %macierz trójkątna górna, bez diagonali

%rnJ = M\b; % do porównania wyników

rk = ones(N,1); % początkowa inicjalizacja wektora rk

DLU = -D\(L+U); %obliczamy -D^-1(L+U), które występuje w każdej iteracji
Db = D\b; % obliczamy czynnik D(-1) * b który jest stały w każdej iteracji


counterS = 0;
intialNorm = norm(M*rk-b);
while norm(M*rk - b) > 10^(-14) %sprawdzamy normee residuum
    counter = counter +1;
    if counter == 1000
        if norm(M*rk - b) > initialNorm
            display("Metoda Jacobi'ego nie zbiega się ");
            break;
        end
    end

    rk = DLU*rk + Db;
end
jacobiTime = toc;

%Gauss-Seidel

D = diag(diag(M)); %tworzymy macierz złożoną tylko z elementów diagonali
L = tril(M, -1); %macierz trójkątna dolna, bez diagonali
U = triu(M, 1); %macierz trójkątna górna, bez diagonali

%rnJ = M\b; % do porównania wyników

rk1 = ones(N,1); % początkowa inicjalizacja wektora rk

DLB = (D + L)\b;

counter = 0;
initialResiduum = norm(M*rk1 - b);
tic;
while norm(M*rk1 - b) > 10^(-14) %sprawdzamy norme residuum
    part = U * rk1;
    rk1 = -(D+L)\part + DLB;
    counter = counter + 1;
    if counter == 1000
        if norm(M*rk1 - b) > initialResiduum
            display("Metoda Gaussa-Seidela się rozbiega");
            break;
        end
    end
end
gsTime = toc;

display("Wbudowana metoda: " + defaultTime);
display("Metoda Jacobi'ego: " + jacobiTime);
display("Metoda Gaussa-Seidela: " + gsTime);
