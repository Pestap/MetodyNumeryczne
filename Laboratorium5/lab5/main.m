
clear all
close all
clc

%zad 1
KV = [5 15 25 33];
[XX, YY] = meshgrid(linspace(0,100,101), linspace(0,100,101));

for K = KV

    [x, y, f, xp, yp] = lazik(K);
    
    %interpolacja wielomianowa
    [p] = polyfit2d(x,y,f);
    [FF] = polyval2d(XX,YY,p);
    
    %interpolacja trygonometryczna

    [pt] = trygfit2d(x,y,f);
    
    [FFt] = trygval2d(XX,YY,pt);


    %wykresy
    figure("Name", "Zad1 K=" + K)
    subplot(2,2,1)

    plot(xp,yp,"-o", 'linewidth', 1);
    title("Trasa łazika");
    xlabel("x[m]")
    ylabel("y[m]")
    grid on;

    subplot(2,2,2)
    plot3(x,y,f,'o');
    title("Zebrane próbki")
    xlabel("x[m]")
    ylabel("y[m]")
    zlabel("f(x,y)")
    grid on;

    %wykresy interpolacji

    subplot(2,2,3)

    surf(XX, YY, FF);
    shading flat
    title("Interpolacja wielomianowa");
    xlabel("x[m]");
    ylabel("y[m]");
    zlabel("f(x,y)");
    grid on

    subplot(2,2,4)

    surf(XX, YY, FFt)
    shading flat
    title("Interpolacja trygonometryczna");
    xlabel("x[m]");
    ylabel("y[m]");
    zlabel("f(x,y)");
    grid on
    
    saveas(gcf, "zad1_K_" + K+ "_184531.png");

end