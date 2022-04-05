clc
clear all
close all
%Liczba parametrów - zad1
a=0;
b=60000;
[xvect_N_bi, xdif_N_bi, fx_N_bi, it_cnt_N_bi] = bisect(a,b,1e-3,@compute_time);

figure("Name", "Wartość przybliżenia N* w zależności od numeru iteracji");
semilogy(xvect_N_bi);
grid on
title("Wartość przybliżenia N* w zależności od numeru iteracji (metoda bisekcji)");
xlabel("Numer iteracji");
ylabel("Liczba parametrów N");
saveas(gcf, "zad1_bisekcja_184531_wykres1.png");

figure("Name", "Wartość różnicy pomiędzy wartościami N w kolejnych iteracjach (metoda bisekcji)");
semilogy(xdif_N_bi);
grid on
title("Wartość różnicy pomiędzy wartościami N w kolejnych iteracjach");
xlabel("Numer iteracji");
ylabel("Różnica w liczbie paremtrów N");
saveas(gcf, "zad1_bisekcja_184531_wykres2.png");

[xvect_N_se, xdif_N_se, fx_N_se, it_cnt_N_se] = secant(a,b,1e-3,@compute_time);

figure("Name", "Wartość przybliżenia N* w zależności od numeru iteracji");
semilogy(xvect_N_se);
grid on
title("Wartość przybliżenia N* w zależności od numeru iteracji (metoda siecznych)");
xlabel("Numer iteracji");
ylabel("Liczba parametrów N");
saveas(gcf, "zad1_sieczne_184531_wykres1.png");

figure("Name", "Wartość różnicy pomiędzy wartościami N w kolejnych iteracjach (metoda siecznych)");
semilogy(xdif_N_se);
grid on
title("Wartość różnicy pomiędzy wartościami N w kolejnych iteracjach");
xlabel("Numer iteracji");
ylabel("Różnica w liczbie parametrów N");
saveas(gcf, "zad1_sieczne_184531_wykres2.png");


%częstotliwość - zad2
a = 0;   
b = 50;

[xvect_imp_bi, xdif_imp_bi, fx_imp_bi, it_cnt_imp_bi] = bisect(a,b,1e-12,@compute_impedance);

figure("Name", "Wartość przybliżenia ω* w zależności od numeru iteracji");
semilogy(xvect_imp_bi);
grid on
title("Wartość przybliżenia ω* w zależności od numeru iteracji (metoda bisekcji)");
xlabel("Numer iteracji");
ylabel("Częstotliwość kątowa [rad/s]");
saveas(gcf, "zad2_bisekcja_184531_wykres1.png");

figure("Name", "Wartość różnicy pomiędzy wartościami ω w kolejnych iteracjach (metoda bisekcji)");
semilogy(xdif_imp_bi);
grid on
title("Wartość różnicy pomiędzy wartościami ω w kolejnych iteracjach");
xlabel("Numer iteracji");
ylabel("Różnica w częstotliwościach kątowych [rad/s]");
saveas(gcf, "zad2_bisekcja_184531_wykres2.png");


[xvect_imp_se, xdif_imp_se, fx_imp_se, it_cnt_imp_se] = secant(a,b,1e-12,@compute_impedance);

figure("Name", "Wartość przybliżenia ω* w zależności od numeru iteracji");
semilogy(xvect_imp_se);
grid on
title("Wartość przybliżenia ω* w zależności od numeru iteracji (metoda siecznych)");
xlabel("Numer iteracji");
ylabel("Częstotliwość kątowa [rad/s]");
saveas(gcf, "zad2_sieczne_184531_wykres1.png");

figure("Name", "Wartość różnicy pomiędzy wartościami x w kolejnych iteracjach");
semilogy(xdif_imp_se);
grid on
title("Wartość różnicy pomiędzy wartościami ω w kolejnych iteracjach (metoda siecznych)");
xlabel("Numer iteracji");
ylabel("Różnica w częstotliwościach kątowych [rad/s]");
saveas(gcf, "zad2_sieczne_184531_wykres2.png");

%predkosc - zad3

a = 0;   
b = 50;

[xvect_vel_bi, xdif_vel_bi, fx_vel_bi, it_cnt_vel_bi] = bisect(a,b,1e-12,@compute_velocity);

figure("Name", "Wartość przybliżenia t* w zależności od numeru iteracji");
semilogy(xvect_vel_bi);
grid on
title("Wartość przybliżenia t* w zależności od numeru iteracji (metoda bisekcji)");
xlabel("Numer iteracji");
ylabel("Czas [s]");
saveas(gcf, "zad3_bisekcja_184531_wykres1.png");

figure("Name", "Wartość różnicy pomiędzy wartościami t w kolejnych iteracjach (metoda bisekcji)");
semilogy(xdif_vel_bi);
grid on
title("Wartość różnicy pomiędzy wartościami t w kolejnych iteracjach");
xlabel("Numer iteracji");
ylabel("Różnice w kolejnych obliczonych wartościach czasu [s]");
saveas(gcf, "zad3_bisekcja_184531_wykres2.png");


[xvect_vel_se, xdif_vel_se, fx_vel_se, it_cnt_vel_se] = secant(a,b,1e-12,@compute_velocity);

figure("Name", "Wartość przybliżenia t* w zależności od numeru iteracji");
semilogy(xvect_vel_se);
grid on
title("Wartość przybliżenia t* w zależności od numeru iteracji (metoda siecznych)");
xlabel("Numer iteracji");
ylabel("Czas [s]");
saveas(gcf, "zad3_sieczne_184531_wykres1.png");

figure("Name", "Wartość różnicy pomiędzy wartościami t w kolejnych iteracjach");
semilogy(xdif_vel_se);
grid on
title("Wartość różnicy pomiędzy wartościami t w kolejnych iteracjach (metoda siecznych)");
xlabel("Numer iteracji");
ylabel("Różnice w kolejnych obliczonych wartościach czasu [s]");
saveas(gcf, "zad3_sieczne_184531_wykres2.png");


%zad3

options = optimset('Display', 'iter');
fzero(@tan, 6, options)


fzero(@tan, 4.5, options)

