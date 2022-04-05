function [xvect,xdif,fx,it_cnt]=secant(a,b,eps,fun)

xvect = [];
xdif = [];
fx = [];
it_cnt = 0;

xNp=a;
xN=b;

xvect(end+1) = xN; % dodanie pierwszego przybliżenia rozwiązania do xvect
fx(end+1) = feval(fun, xN); % dodanie wartosci

for i = 1:1000

    yNp = feval(fun,xNp); % obliczenie wartosci funkcji w N-1
    yN = feval(fun,xN); % obliczenie wartosci funkcji w N
   
    xNn = xN - (yN/((yN - yNp)/(xN-xNp))); % obliczenie N+1
    
    xvect(end+1) = xNn; % dodanie N + 1 do xvect

    yNn = feval(fun,xNn);
    fx(end+1) = yNn;
    if abs(yNn) < eps
        it_cnt = i;
        break
    end
    xNp = xN;
    xN = xNn;

end
% obliczanie diff
for i = 1:length(xvect)-1
    xdif(i) = abs(xvect(i+1) - xvect(i));
end

end

