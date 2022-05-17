clc
clear all
close all

warning('off','all')

load trajektoria1

%zadania 1,2,3,4
N = 50;

[ wsp_wielomianu, xa ] = aproksymacjaWiel(n,x,N);  % aproksymacja wsp. 'x'.
[ wsp_wielomianu, ya ] = aproksymacjaWiel(n,y,N);  % aproksymacja wsp. 'y'.
[ wsp_wielomianu, za ] = aproksymacjaWiel(n,z,N);  % aproksymacja wsp. 'z'.


figure("Name", "Dane z systemu lokalizacji N="+N)
plot3(x,y,z,'o');
grid on
axis equal
xlabel("x [m]");
ylabel("y [m]");
zlabel("z [m]");
title("Dane z systemu lokalizacji N="+N)
saveas(gcf, "184531_Pesta_zad2.png")


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
saveas(gcf, "184531_Pesta_zad4.png")
hold off



