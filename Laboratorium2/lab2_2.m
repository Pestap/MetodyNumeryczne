


a = 1;
r_max = a/4;
n_max = 1000;

X = 0;
Y = 0;
R = 0;
x = [];
y = [];
r = [];
p = [];
pSum = []
tries = []
n = 0;


while n < n_max

    fitsInA = false;
    numberOfTries = 0;
    while not(fitsInA)
       
        R = rand()*r_max;
        X = rand()*a;
        Y = rand()*a;
        
        if X + R < a && X - R > 0 && Y + R < a && Y-R > 0
            fitsInA = true
        end
         numberOfTries = numberOfTries + 1;
    end
    
    intersects = false;
    for i = 1:n
        distanceBetweenCenters = sqrt((x(i)-X)^2 + (y(i) - Y)^2);
        radiusSum = r(i) + R;
        if distanceBetweenCenters <radiusSum
            intersects = true
            break;  
        end
        

    end
    if not(intersects)
        n = n+1;
        area = pi*R*R;
        plot_circ(X,Y,R);
        x(n) = X;
        y(n) = Y;
        r(n) = R;
        p(n) = area;
        tries(n) = numberOfTries;
        if n == 1
            pSum(n) = area;
        else
            pSum(n) = pSum(n-1) + area;
        end

        axis equal
        hold on
        fprintf(1, ' %s%5d%s%.3g\r ', 'n =',  n, ' S = ', area);
        pause(0.01);
    end

end
hold off

figure('Name', 'Powierzchnia łączna');
semilogx(pSum);

figure('Name', 'Liczba prób');
loglog(cumsum(tries))
