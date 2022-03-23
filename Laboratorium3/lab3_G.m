load Dane_Filtr_Dielektryczny_lab3_MN.mat

%wbudowana metoda
tic;
r = M\b;
defaultTime = toc;

N = size(M,1);

%Jacobi
tic
D = diag(diag(M)); %tworzymy macierz złożoną tylko z elementów diagonali
L = tril(M) - D; %macierz trójkątna dolna, bez diagonali
U = triu(M) - D; %macierz trójkątna górna, bez diagonali

%rnJ = M\b; % do porównania wyników

rk = ones(N,1); % początkowa inicjalizacja wektora rk

DLU = -D\(L+U); %obliczamy -D^-1(L+U), które występuje w każdej iteracji
Db = D\b; % obliczamy czynnik D(-1) * b który jest stały w każdej iteracji
while norm(M*rk - b) > 10^(-14) %sprawdzamy normee residuum
    rk = DLU*rk + Db;
end
jacobiTime = toc;

%Gauss-Seidel

D = diag(diag(M)); %tworzymy macierz złożoną tylko z elementów diagonali
L = tril(M) - D; %macierz trójkątna dolna, bez diagonali
U = triu(M) - D; %macierz trójkątna górna, bez diagonali

%rnJ = M\b; % do porównania wyników

rk1 = ones(N,1); % początkowa inicjalizacja wektora rk

DLB = (D + L)\b;

tic;
while norm(M*rk1 - b) > 10^(-14) %sprawdzamy normee residuum
    part = U * rk1;
    rk1 = -(D+L)\part + DLB;
end
gsTime = toc;

display("Wbudowana metoda: " + defaultTime);
display("Metoda Jacobi'ego: " + jacobiTime);
display("Metoda Gaussa-Seidela: " + gsTime);
