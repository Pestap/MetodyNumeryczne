clc
clear all
close all
load P_ref

%przedział w którym całkujemy
a = 0;
b = 5;

blad_prostkaty = [];
blad_trapezy = [];
blad_simpson = [];
blad_mc = [];

%wykres funkcji awaria

vals = []
for i = 1:20
    vals(end+1) = awaria(i)
end

plot(vals)

%metoda prostokątów
N_arr = 5:50:10^4;
for N = N_arr
    dx = (b-a)/N; % szerokosc prostokata
    wynik_prostokaty = 0;

    for i = 0:N
        x_1 = a+dx*i;
        x_2 = a+dx*(i+1);
        x_mid = (x_1 + x_2)/2;
        wynik_prostokaty = wynik_prostokaty + awaria(x_mid)*dx;
    end
    blad_prostkaty(end+1) = abs(wynik_prostokaty - P_ref);
end


%metoda trapezów
for N = N_arr
    dx = (b-a)/N; % wysokosc trapezu
    wynik_trapezy = 0;

    for i = 0:N
        x_1 = a+dx*i;
        x_2 = a+dx*(i+1);
        wynik_trapezy = wynik_trapezy + (awaria(x_1) + awaria(x_2))*dx/2;
    end
    blad_trapezy(end+1) = abs(wynik_trapezy - P_ref);
end


%metoda Simpsona

for N = N_arr
    dx = (b-a)/N; % szerokosc przedziału
    wynik_simpson = 0;

    for i = 0:N
        x_1 = a + dx*i;
        x_2 = a + dx*(i+1);
        x_mid = (x_1 + x_2)/2;
        wynik_simpson = wynik_simpson + dx/6*(awaria(x_1) + 4*awaria(x_mid) + awaria(x_2));
    end
    blad_simpson(end+1) = abs(wynik_simpson - P_ref);
end


%metoda Monte Carlo
fmax = awaria(b);
fmin = 0;

ydif = fmax - fmin;
xdif = b-a

for N = N_arr
    area = xdif*ydif;
    number_of_points = 0;
    for i = 1:N
        x = rand()*xdif + a;
        y = rand() * ydif  + fmin;
        if y>= fmin && y <= awaria(x)
            number_of_points = number_of_points + 1;
        end
    end
    wynik_monte_carlo = number_of_points/N * area;
    blad_mc(end+1) = abs(wynik_monte_carlo - P_ref);
end

figure("name", "Błąd całkowania w różnych metodach");

loglog(N_arr, blad_prostkaty);
hold on
loglog(N_arr, blad_trapezy);
loglog(N_arr, blad_simpson);
loglog(N_arr, blad_mc);
hold off
title("Błąd całkowania w różnych metodach");
ylabel("Wartość błędu");
xlabel("Licbza przedziałów");
legend("Metoda prostokątów", "Metoda trapezów", "Metoda Simpsona", "Metoda Monte Carlo");
saveas(gcf, 'blad_calkowania.png');



%czasy wykonania
N = 10^7;
czas_p = 0;
czas_t = 0;
czas_s = 0;
czas_mc = 0;



%prostokatow
tic;
dx = (b-a)/N; % szerokosc prostokata
wynik_prostokaty = 0;

for i = 0:N
    x_1 = a+dx*i;
    x_2 = a+dx*(i+1);
    x_mid = (x_1 + x_2)/2;
    wynik_prostokaty = wynik_prostokaty + awaria(x_mid)*dx;
end
czas_p = toc;



%trapezów
tic;
dx = (b-a)/N; % wysokosc trapezu
wynik_trapezy = 0;

for i = 0:N
    x_1 = a+dx*i;
    x_2 = a+dx*(i+1);
    wynik_trapezy = wynik_trapezy + (awaria(x_1) + awaria(x_2))*dx/2;
end
czas_t = toc;


%simspon
tic;
dx = (b-a)/N; % szerokosc przedziału
wynik_simpson = 0;

for i = 0:N
    x_1 = a + dx*i;
    x_2 = a + dx*(i+1);
    x_mid = (x_1 + x_2)/2;
    wynik_simpson = wynik_simpson + dx/6*(awaria(x_1) + 4*awaria(x_mid) + awaria(x_2));
end
czas_s = toc;

%Monte Carlo
tic;
qrea = xdif*ydif;
number_of_points = 0;
for i = 1:N
    x = rand() * xdif + a;
    y = rand() * ydif  + fmin;
    if y>= fmin && y <= awaria(x)
        number_of_points = number_of_points + 1;
    end
end
wynik_monte_carlo = number_of_points/N * area;
czas_mc = toc;




figure("name", "Czas wykonania dla N=" +N);

labels = categorical({'Prostokąty', 'Trapezy', 'Simpson', 'Monte Carlo'});
labels = reordercats(labels, {'Prostokąty', 'Trapezy', 'Simpson', 'Monte Carlo'});
bar(labels , [czas_p, czas_t, czas_s, czas_mc]);
title("name", "Czas wykonania dla N=" +N);
ylabel("Czas działania [s]");
