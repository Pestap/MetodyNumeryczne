%zadanie 5
clc
clear all
close all

warning('off','all')
load trajektoria2.mat

N = 1;

%wyszukanie zadowalającego N (dla którego błąd będzie mniejszy niż zadana
%wartość epsilon

epsilon = 7 * 10^-3;
while true
    M = size(n,2);
    xa = aprox_tryg(n,x,N);  % aproksymacja wsp. 'x'.
    ya = aprox_tryg(n,y,N);  % aproksymacja wsp. 'y'.
    za = aprox_tryg(n,z,N);  % aproksymacja wsp. 'z'.

    err_temp = 0;
    err_x = sqrt(sum((x - xa).^2)) / M;
    err_y = sqrt(sum((y - ya).^2)) / M;
    err_z = sqrt(sum((z - za).^2)) / M;

    err_temp = err_x + err_y + err_z;
    
    if err_temp < epsilon
        break
    end

    N = N+1;
end


xa = aprox_tryg(n,x,N);  % aproksymacja wsp. 'x'.
ya = aprox_tryg(n,y,N);  % aproksymacja wsp. 'y'.
za = aprox_tryg(n,z,N);  % aproksymacja wsp. 'z'.

figure("Name", "Aproksymacja trygonometryczna położenia drona dla N="+N)

plot3(x,y,z,'o');
hold on
plot3(xa,ya,za,LineWidth=4);
axis equal
grid on
xlabel("x [m]");
ylabel("y [m]");
zlabel("z [m]");
title("Aproksymacja trygonometryczna położenia drona dla N="+N)
saveas(gcf, "184531_Pesta_zad7.png")
hold off


%wykres błedu

err = [];
M = size(n,2);


for N=1:71
    xa = aprox_tryg(n,x,N);  % aproksymacja wsp. 'x'.
    ya = aprox_tryg(n,y,N);  % aproksymacja wsp. 'y'.
    za = aprox_tryg(n,z,N);  % aproksymacja wsp. 'z'.

    err_temp = 0;
    err_x = sqrt(sum((x - xa).^2)) / M;
    err_y = sqrt(sum((y - ya).^2)) / M;
    err_z = sqrt(sum((z - za).^2)) / M;

    err_temp = err_x + err_y + err_z;

    err(end+1) = err_temp;
end

figure("Name", "Wykres błędu");
semilogy(err)
grid on
title("Błąd aproksymacji trygonometrycznej");
xlabel("Wartośći N");
ylabel("Wartość błędu");
saveas(gcf, "184531_Pesta_zad7_b.png");
