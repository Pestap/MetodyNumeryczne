clc
clear all
close all

%impedance
a = 0;   
b = 50;

[xvect_imp_bi, xdif_imp_bi, fx_imp_bi, it_cnt_imp_bi] = bisect(a,b,1e-12,@compute_impedance);
plot(xdif_imp_bi);



[xvect_imp_se, xdif_imp_se, fx_imp_se, it_cnt_imp_se] = secant(a,b,1e-12,@compute_impedance);

asd = fzero(@compute_impedance,50);
display("koniec");