

# a2 + b2 = c2
import math
a = 2
b = 3
c = math.sqrt(a ** 2 + b ** 2)
print(c)

#Formula : (a + b)2 = a^2 + b^2 + 2ab


a=2
b=3
result = math.sqrt((a**2) + (b**2) + (2 * a * b))
print(result)

#Formula : (a – b)2 = a^2 + b^2 – 2ab
a=5
b=2
result= (a**2) + (b**2) - (2 * a *b)
print(result)

# Formula : a2 – b2 = (a-b)(a+b)

a=6
b=5
result= (6-5) * (6+5)
print(result)

#Formula : (a + b)3 = a3 + 3ab(a+b) + b3

a=3
b=5
result= (a**3) + (3*3*5) * (3+5)+ (b**3)
print(result)

#Formula : (a – b)3 = a3 – 3a2b + 3ab2 – b3

a=4
b=5
result= (4**3) - (3*(a**2)*b) + (3*a*(b**2)) - (b**3)
print(result)