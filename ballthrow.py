import math

print('Compund Interests')
h = float(input('height in m h='))
v0 = float(input('initial speed in m/s v0='))
alpha = float(input('angle alpha in degree='))

#Angle input in degree, also 0-360° und soll umgerechnet werden in 0-2pi radiant
new_alpha = math.radians(alpha)
g = 9.81

t_flight = (v0*math.sin(new_alpha)+math.sqrt(((v0*math.sin(new_alpha))**2)+ (2*g*h)))/g
d = v0*math.cos(new_alpha)*t_flight

print (f" The time of flight is {(t_flight)} seconds and the distance of the throw is {d} meters")
#print(round(t_flight,2),round(d,2)) -> um zu runden und 2 nachkomma zahlen zu haben
#nice 