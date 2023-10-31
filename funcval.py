#Assignment 2
import math
xmin=int(input('xmin='))
xmax=int(input('xmax='))
dx=float(input('The step size dx for the function above^ should be? dx='))

value_table = []
x = xmin

while x <= xmax:
    f = math.cos((x * math.pi) / 8)
    value_table.append((x, f))  
    x += dx

print("x\ty")
for x, y in value_table:
    print(f"{x}\t{y}")