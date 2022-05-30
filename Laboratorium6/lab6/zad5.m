%zadanie 5
clc
clear all
close all

warning('off','all')
load trajektoria2.mat

%N = 45;
N = 60;

[ wsp_wielomianu, xa ] = aproksymacjaWiel(n,x,N);  % aproksymacja wsp. 'x'.
[ wsp_wielomianu, ya ] = aproksymacjaWiel(n,y,N);  % aproksymacja wsp. 'y'.
[ wsp_wielomianu, za ] = aproksymacjaWiel(n,z,N);  % aproksymacja wsp. 'z'.

figure("Name", "Aproksymacja wielomianowa położenia drona dla N="+N)

plot3(x,y,z,'o');
hold on
plot3(xa,ya,za,LineWidth=4);
axis equal
grid on
xlabel("x [m]");
ylabel("y [m]");
zlabel("z [m]");
title("Aproksymacja wielomianowa położenia drona dla N="+N)
saveas(gcf, "184531_Pesta_zad5.png")
hold off


%wykres błedu

err = [];
M = size(n,2);


for N=1:71
    [ wsp_wielomianu, xa ] = aproksymacjaWiel(n,x,N);  % aproksymacja wsp. 'x'.
    [ wsp_wielomianu, ya ] = aproksymacjaWiel(n,y,N);  % aproksymacja wsp. 'y'.
    [ wsp_wielomianu, za ] = aproksymacjaWiel(n,z,N);  % aproksymacja wsp. 'z'.

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
title("Błąd aproksymacji wielomianowej");
xlabel("Wartośći N");
ylabel("Wartość błędu");
saveas(gcf, "184531_Pesta_zad5_b.png");

