"""Pseudocode
binary base, can be changes to any base
procedure karatsuba(x,y, length(x,y)):
    if n==1:
        return x*y
    else:
        m = n//2
        x1, x0 = (x/2**m , xmod(2**m))
        y1, y0 = (y/2**m , ymod(2**m))
        p = karatsuba(x1,y1,m)
        q = karatsuba(x0,y0,m)
        r = karatsuba(x1-x0 , y1-y0)
        return p*(2**n)+(p+q-r)*(2**(m))+q"""

"""Above is easier for complexity analysis: Originally, it was suggested that 3 O(n) multiplications like the following be performed:
(x1+x0)(y1+y0) = x1y1+(x0y1+y0x1)+x0y0 = r (say)
Then, x0y1+y0x1 = r - x1y1-x0y0    and 
if x = x1*(2**(n//2))+x0 and x = y1*(2**(n//2))+y0, then
xy = x1y12**n + (x1y0+y1x0)2**(n//2) + x0y0 """

def assign_values(x,y):  ## Values are base 10 here, for any other base, change where indicated, this is a helper function
  n = max(len(str(x)), len(str(y)))//2
  x1, x0 = x//(10**n) , x%(10**n)  ## change 10 to any other number corresponding to base
  x1_plus_x0 = x1+x0      
  y1, y0 = y//(10**n) , y%(10**n)
  y1_plus_y0 = y1+y0
  r = karatsuba(x1,y1)
  s = karatsuba(x0,y0)
  
  return n, x1_plus_x0, y1_plus_y0, r , s

def karastuba(x,y):
  if x<10 and y<10:
    return x*y
  else:
    var1, var2, var3, var4, var5 = assign_values(x,y)
    x0y1_plus_y0x1 = karatsuba(var2, var3)-r-s
    return (10**(var1*2))*(r)+(x0y1_plus_y0x1)*(10**var1)+s
