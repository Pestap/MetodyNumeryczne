
clear all
close all
clc

%zad 1

divPol = [];
divTr = [];
FF_prev = 0;
FFt_prev = 0;
for K = 5:45

    [x, y, f, xp, yp] = lazik(K);
    
    %interpolacja wielomianowa
    [p] = polyfit2d(x,y,f);
    
    [XX, YY] = meshgrid(linspace(0,100,101), linspace(0,100,101));

    [FF] = polyval2d(XX,YY,p);

    %interpolacja trygonometryczna

    [pt] = trygfit2d(x,y,f);
    
    [XXt, YYt ]= meshgrid(linspace(0,100,101), linspace(0,100,101));
    [FFt] = trygval2d(XXt,YYt,pt);

    if K == 5
        FF_prev = FF;
        divPol(end+1) = max(max(FF));
        FFt_prev = FFt;
    else
        divPol(end+1) = max(max(abs(FF - FF_prev)));
        divTr(end+1) = max(max(abs(FFt - FFt_prev)));
        FF_prev = FF;
        FFt_prev = FFt;
    end

end
figure("Name", "Zbieżność interpolacji wielomianowej");
plot(5:45, divPol);
grid on 
title("Zbieżność interpolacji wielomianowej");
xlabel("Liczba punktów pomiarowych K");
ylabel("Maksymalna różnica wartości interpolowanych funkcji");
saveas(gcf, "zad2_wielomianowa_184531.png");

figure("Name", "Zbieżność interpolacji trygonometrycznej");
plot(6:45, divTr);
grid on 
title("Zbieżność interpolacji trygonometrycznej");
xlabel("Liczba punktów pomiarowych K");
ylabel("Maksymalna różnica wartości interpolowanych funkcji");
saveas(gcf, "zad2_trygnonometryczna_184531.png");






