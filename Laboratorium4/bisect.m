function [xvect,xdif,fx,it_cnt]=bisect(a,b,eps,fun)

xvect = [];
xdif = [];
fx = [];
it_cnt = 0;


for i = 1:1000
    x = (a+b)/2;
    y = feval(fun,x); % pobranie wartości funkcji w x 

    xvect(end+1) = x; % dodanie x do xvect
    fx(end+1) = y; % dodanie y do fx

    if abs(y) < eps || abs(a-b) < eps % gdy rozwiązanie nas satysfakcjonuje
        it_cnt = i;
        break;
    elseif feval(fun, a) * y < 0 % wybór nowych a i b
            b = x;
    else
            a = x;
    end

end
% obliczanie diff
for i = 1:length(xvect)-1
    xdif(i) = abs(xvect(i+1) - xvect(i));
end

end

