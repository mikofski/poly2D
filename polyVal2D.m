function f = polyVal2D(p,x,y,n,m)
%POLYVAL2D Evaluate a 2-D polynomial using Horner's method.
%   F = POLYVAL2D(P,X,Y) evaluates the 2-D polynomial P at the
%   points specified by X and Y, which must be the same
%   dimensions. The output F will be the same dimensions as X and 
%   Y. N and M specify the order of X and Y respectively.
% See also: POLYFITN by John D'Errico on MathWorks MATLAB Central FEX
% http://www.mathworks.com/matlabcentral/fileexchange/34765-polyfitn
% TODO: check input args
f = p(1);
for ni = 1:n
    f = f.*x+p(1+ni);
end
for mi = 1:m
    mj = (n+1)*mi+1
    g = p(mj);
    for ni = 1:n
        g = g.*x+p(mj+ni);
    end
    f = f.*y+g;
end
