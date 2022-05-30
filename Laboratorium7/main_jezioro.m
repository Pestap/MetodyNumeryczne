clc
clear all


%------------------------------------------
load dane_jezioro   % dane XX, YY, FF sa potrzebne jedynie do wizualizacji problemu. 
surf(XX,YY,FF)
shading interp
axis equal
%------------------------------------------


%------------------------------------------
% Implementacja Monte Carlo dla f(x,y) w celu obliczenia objetosci wody w zbiorniku wodnym. 
% Calka = ?
% Nalezy skorzystac z nastepujacej funkcji:
% z = glebokosc(x,y); % wyznaczanie glebokosci jeziora w punkcie (x,y),
% gdzie x i y sa losowane
%------------------------------------------

maxx = 100;
maxy = 100;
minx = 0;
miny = 0;
maxz = 0;
minz = -50;

fmax = 0;
fmin = 44;

N_1 = 0;
N = 1e5;
for i = 1:N
    %losujemy punkt
    x = rand()*(maxx - minx) + minx;
    y = rand()*(maxy - miny) + miny;
    z = rand()*(maxz - minz) + minz;
    
    %wyznaczamy wartosc funkcji w tym punkcie
    fxy = glebokosc(x,y);

    %sprawdzamy czy wylosowany wczesniej wartosc jest NAD dnem jeziora
    if z<= fmax && z >= fxy
        N_1 = N_1 + 1;
    end
end

result = (N_1/N)*((maxx-minx) * (maxy-miny) *(maxz - minz))
