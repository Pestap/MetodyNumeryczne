clc
clear all
close all

%A = rand(4,4);  % system Ax = b
b = rand(12,1);
A = [1 0 0 0 0 0 0 0 0 0 0 0 ; 1 431 185761 80062991 0 0 0 0 0 0 0 0
     0 1 862 557283 0 -1 0 0 0 0 0 0 ; 0 0 2 2586 0 0 -2 0 0 0 0 0 ;
    0 0 0 0 1 0 0 0 0 0 0 0 ; 0 0 0 0 1 431 185761 80062991 0 0 0 0 ;
    0 0 0 0 0 1 862 557283 0 -1 0 0 ; 0 0 0 0 0 0 2 2586 0 0 -2 0 ;
    0 0 0 0 0 0 0 0 1 0 0 0 ; 
    0 0 0 0 0 0 0 0 1 431 185761 80062991
    0 0 2 0 0 0 0 0 0 0 0 0 ;
    0 0 0 0 0 0 0 0 0 0 0 2586
    ]


x_ref = A\b;    % x reference 
[m, n] = size(A); 
L=eye(n); 
P=eye(n);       % permutation matrix
U=A;
   
for k=1:m-1
% find pivot
   [ pivot ind]=max(abs(U(k:m,k)));
   ind = ind+k-1;
   
% interchange rows
   U([k,ind],k:m)=U([ind,k],k:m);
   L([k,ind],1:k-1)=L([ind,k],1:k-1);
   P([k,ind],:)=P([ind,k],:);
   
% standard LU
   for j=k+1:m
       L(j,k)=U(j,k)/U(k,k);
       U(j,k:m)=U(j,k:m)-L(j,k)*U(k,k:m);
   end
end
   
test = A\b
x = (U \ (L\(P * b)))  % LU after pivot, note the Permutation matrix
norm(x - x_ref);		    % error 