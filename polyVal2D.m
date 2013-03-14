function f = polyVal2D(p,x,y,n,m)
%POLYVAL2D Evaluate a 2-D polynomial using Horner's method.
%   F = POLYVAL2D(P,X,Y) evaluates the 2-D polynomial P at the
%   points specified by X and Y, which must be the same
%   dimensions. The output F will be the same dimensions as X and 
%   Y. N and M specify the order of X and Y respectively.
% TODO: check input args
f = p(1);
for ni = 1:n
    f = f.*x+p(1+ni);
end
npp = n+1;
for mi = 1:m
    g = p(npp*mi+1);
    for ni = 1:n
        g = g.*x+p(npp*mi+1+ni);
    end
    f = f.*y+g;
end