#Assignment 2
n = int(input('n='))
x = []
for i in range(0,n):
    i=i+1
    x.append(i)
Produkt = 1
for j in range(1,n+1):    
    Produkt*=j
print(x);
print('The sum of numbers up to',n,'is',sum(x))
print('The product of all the numbers up to',n,'is',Produkt)
   