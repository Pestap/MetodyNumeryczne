function [value] = compute_velocity(t)

g = 9.81;
m0 = 150000;
q= 2700;
u = 2000;

velocity = u * log(m0/(m0 - q * t)) - g *t;
value = velocity - 750;
end