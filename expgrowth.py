#First fomular
import math

print('Compund Interests')
P = float(input('Starting amount P='))
r = float(input('annual interest r='))
t = float(input('numer of years t='))

result_c= P*math.exp(r*t)
print (f"{result_c} is the amount of money you would have if you invested it at a given interest of {r} for {t} years")

#Second formula
import random
n = random.randint (1,365)
# I made n a random number between 1 and 365 because in the task it was asked for a discrete number of times per year, which doesnt state a static number, but more random
result_d= P*(1+(r/n))**(n*t)
print (f"{result_d} is the discrete compound interest with a random n. Not included is the chance of multiple times per day")
print (f"{n} ist das random n")

# I cant anwser it truthfully because I dont fully understand, but i would say if n is maybe close to r
# because then ()**nt would be basically ()**rt and if r=n then (1+r/n) would be 2, which is close to e (2.718 or something)
# the smallest n can be is 1 if I understood the question correctly 