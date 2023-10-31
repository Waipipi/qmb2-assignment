import math

# find solutions x1,x2 of the equation x**2+p*x+q=0

print('Find solutions for x**2+p*x+q=0')
p = float(input('p='))
q = float(input('q='))

discriminant = p*p - 4.0*q
d = math.sqrt(discriminant)
solution1 = ( (-p+d)/2.0 )
solution2 = ( (-p-d)/2.0 )

print(solution1,solution2)
