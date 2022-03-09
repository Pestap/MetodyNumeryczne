a = 1;
r_max = a/3;
n_max = 1000;

X = 0;
Y = 0;
R = 0;
x = zeros(1,n_max);
y = zeros(1,n_max);
r = zeros(1,n_max);
p = zeros(1,n_max);
pSum = zeros(1,n_max);
tries = zeros(1, n_max);
n = 0;
numberOfTries = 0;

while n < n_max

    fitsInA = false;
    
    while not(fitsInA)
       
        R = rand*r_max;
        X = rand*a;
        Y = rand*a;
        
        if X + R < a && X - R > 0 && Y + R < a && Y-R > 0
            fitsInA = true;
        end

         numberOfTries = numberOfTries + 1;
    end
    
    intersects = false;
    for i = 1:n
        distanceBetweenCenters = sqrt((x(i)-X)^2 + (y(i) - Y)^2);
        radiusSum = r(i) + R;
        if distanceBetweenCenters < radiusSum
            intersects = true;
            break;  
        end
    end

    if not(intersects)
        n = n + 1;
        area = pi*R*R;
        plot_circ(X,Y,R);
        x(n) = X;
        y(n) = Y;
        r(n) = R;
        p(n) = area;
        tries(n) = numberOfTries;
        numberOfTries = 0;
        if n == 1
            pSum(n) = area;
        else
            pSum(n) = pSum(n-1) + area;
        end

        axis equal
        hold on
        %fprintf(1, ' %s%5d%s%.3g\r ', 'n =',  n, ' S = ', area);
        pause(0.01);
    end

end
hold off


title('Okręgi w kwadracie');
saveas(gcf, 'okregi.png');

figure('Name', 'Powierzchnia łączna');


semilogx(pSum);
title('Powierzchnia łączna');
xlabel('n-ty okrąg');
ylabel('Powierzchnia');
saveas(gcf, 'powierzchnia.png');
figure('Name', 'Liczba prób');
loglog(cumsum(tries) ./ ((1:n_max)))
title('Liczba prób');
xlabel('n-ty okrąg');
ylabel('liczba prób');
saveas(gcf, 'liczbaprob.png');
