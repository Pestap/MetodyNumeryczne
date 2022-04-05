function [value] = compute_time( N )

time = (N^(1.43) + N^(1.14)) /1000;
value = time - 5000;

end