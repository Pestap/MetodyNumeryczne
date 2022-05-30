function result = awaria(t)
    ni = 10;
    sigma = 3;

    result = 1/(sigma*sqrt(2*pi)) * exp(-(t-ni)^2/(2*sigma^2));
end