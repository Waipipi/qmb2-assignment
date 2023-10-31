# Volresung 3, if statements and loops, conditionals
# if <boolean expression>:
#	tab direkt und dann statement
#	tab statement

#x = float (input("x="))

#if (x<0):
 #   x = -x
  #  print ("x is negative")
# hier wird jede negative zahl
#print (x)

#x=float(input("x="))
#y=float(input("y="))

#print(x,y)

#if x>y :
#	temp=x
#	x=y
#	y=temp
#	print(x,y)
# temp is switching the position between x and y? Damit X immer kleiner als y sein soll
#print("Done.")

#x=float(input("x="))
#y=float(input("y="))

#if x>y:
 #   maximum=x
#else:
 #   maximum=y
#print (maximum)		#sehr cool :D

#import random

#r=random.randrange(0,2)	#durch randrage gibt es nur 0 und 1 und keine 2. Daher ist die chance 50/50
#if(r==0):
 #   print('Heads')
#else:
#    print('Tails')

#i = 4
#while (i<=8):
 #   print(str(i)+"-th Hello")
  #  i=i+1
   
#n=int(input("n="))	#Einfache Möglichkeit die eine Reihe mit Nummerierung zu erstellen
#power=1		#So könnte auch Fibonacci gehen. Ich möchte wissen wie groß bei dem 7ten Schritt die Reihe ist
#i=0		# die reihe gibt 2^n an
#while i<=n :
#	print(i, power)
#	power=2*power;
#	i=i+1

#for i in range (4,9):
 #   print(str(i)+"-th Hello")


#n=int(input("n="))

#for i in range(1,n+1):
    # Write the ith line
 #   for j in range(1,n+1):
        # Write the jth entry in the ith line
  #      if (i % j == 0) or (j%i)==0:
   #         print('*',end=' ')
    #    else:
     #       print(' ',end=' ')
    #print(i)

#income=float(input("income="))

#if income<10000:
 #   rate=0.0
#else:
 #   if income<20000:
  #      rate=0.10
   # else:
    #    if income<40000:
     #       rate=0.20
      #  else:
       #     rate=0.40

#tax=income*rate
#print("Your tax rate is "+str(100*rate)+"%")
#print("You have to pay "+str(tax)+"€ in taxes.")
        


#income=float(input("income=")) #gleiche wie obererrcode direkt hierüber, aber vereinfacht

#if income<10000:
 #   rate=0.0
#elif income<20000:
 #   rate=0.10
#elif income<40000:
 #   rate=0.20
#else:
 #   rate=0.40

#tax=income*rate
#print("Your tax rate is "+str(100*rate)+"%")
#print("You have to pay "+str(tax)+"€ in taxes.")

#studentNames = ['Alice','Bob','Carl','Doris']
#for index, name in enumerate(studentNames):
 #   print(index,"Hi ",name,"! How are you?")
    
#studentAge = {'Alice':21,'Bob':23,'Carl':27}
#for i in studentAge:
 #   print(i)
  #  print("Name=%s,Age=%d"%(i,studentAge[i]))

#for i,j in studentAge.items():
 #   print("Name=%s,Age=%d"%(i,j))		ein coooler Weg den output so darzustellen bei einer Liste (dictionary)
 
#j=0;
#for i in range(5):
 #   j=j+2
  #  if j==6:
   #     break
    #print('i=',i,',j=',j) # wichtig um loops fürhzeitig zu stoppen wenn bereits ein Wert erreicht wurde
    #aber der Bereich noch geht( range5) aber höre bei 2 auf

#j=0;	#; damit es im Shell nicht angezeigt wird. Wie wenn ich viele Werte definiere am Anfang
#for i in range(5):
 #   j=j+2
  #  if j==6:
   #     continue
    #print('i=',i,',j=',j)	# bei 6 wird dieser Schritt übersprungen wegen continue
    
#a = 5.
#b = 2.	#bei b = 0 kommt ein fehler und daher except
#try:
 #   divison = a/b
  #  print(divison)
#except:
 #   print("An error occured")	#ich kann am anfang unter b noch schreiben division = 'empty'
    # Ich schreibe noch eine line ganz unten print(division). Wenn ich b 02 habe, geht die rechnung
    #bei try und auch mein letztens print division wird überschrieben. Wenn b=0 ist, geht der TRY nicht
    # und das division das ich am Anfang definiert habe bleibt und würde mir ganz am Ende außerhalb der except line zeigen'empty'
    
#try:
 #userInput1= int(input("Please enter a number:"))
 #userInput2= int(input("Please enter another number:"))
 #answer=userInput1/userInput2
 #print("The answer is:", answer)
 #myFile = open("missing.txt", 'r')
#except ValueError:
 #print("Error: You did not enter a number")
#except ZeroDivisionError:
 #print("Error: Cannot divide by zero")
#except Exception as e:
 #print("Unknown error: ",e)
		#antworten für verschiedene fehler


    # Computing sqrt of a positive number c is equivalent
# to finding the positive root of the function f(x)=x**2-c
# This is the special case implemented here.
import math
# A variable defining the desired precision for the estimate
EPSILON = 1e-15

# Input the number you want to calculate the square root
c = float(input("number:"))
 
t = c # set the input as the initial value for the iteration
i = 1 # iteration counter

# if t=c/t then t is the square root of c
# The while loop as long as the difference t-c/t is larger then the
# desired precision 
while abs(t - c/t) > (EPSILON * t):
    # Replace t by the average of t and c/t.
    print("Iteration ",i, ", Estimate: ", t)
    t = (c/t + t) / 2.0
    i=i+1

print("\n Final result:",t)
print(" math.sqrt(c)=",math.sqrt(c))



import random
stake  = int(input("stake="))
goal   = int(input("goal="))
trials = int(input("trials="))

# Run trialCount experiments that start with stake and terminate on
# 0 or goal.
bets = 0
wins = 0
for t in range(trials):
    # Run one experiment.
    cash = stake
    while cash > 0 and cash < goal: #einfach geil geschrieben	
        # Simulate one bet.
        bets += 1
        if random.random() < 0.5:
            cash += 1
        else:
            cash -= 1
    if cash == goal:
        wins += 1

print("-------- Results ---------")
print('Win ratio:'+str(wins/trials))
print('Avg # bets per trial: ' + str(bets//trials))



    

    
