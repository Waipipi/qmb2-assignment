#27_10
#Functions are

#def maximum(x,y):
#	if(x>y):
#		maximum=x
#	else:
#		maximum=y
##
#	return maximum
#
#a=10
#b=12
#m=maximum(a,b)
#print(m)		#nochmal mit dem debug käfer die reihefolge durchegehn

#def SumMulArray(array):
   # totalsum = array[0]
   # totalmul = array[0]
   # for i in range(1,len(array)):	#wir starten nicht bei 0, weil wir schon die 1 ertse zahl in line18719 definiert haben und würden wir mit 0 starten, würde die multiplikation nicht funktionieren
   #     totalsum+=array[i]
  #      totalmul*=array[i]
        
 #   return [totalsum,totalmul]


#array=[5.0,1.5,3.3,2.1]
#result=SumMulArray(array)
#print(result)

def func(s):
    s +='Added string (inside).'	#the s wird nur in der funktion verändert und bleibt außerhalb der Funktion gleich
    print("Inside Function:", s)	#will ich das auch außen das s verändert wird, muss ich return s schreiben, um das ergebnis aus einer Funktion rauszunehmen
  
# Global scope
s = "This is a string (outside). "
func(s)
print("Outside Function:",s)


import random

def CoinFlips():
    flipResults=[]    
    isHeads=bool()
    no_flips=2
    for i in range(no_flips):
        if(random.random()<0.5):
            isHeads=True
        else:
            isHeads=False

        flipResults.append(isHeads)
    return flipResults
no_flips=10
flipResults=CoinFlips()
print(flipResults)
# könnte auch bei CoinFlips(no_flips) machen sowohl oben als auch unten, damit man sicher ist oder auch mit input arbeiten kann
#WICHTIG. Alle Übungen mit Funktionen hatten immer am Ende ein return'flipresults/maximum/Sumarray' oder so
# und nach dem return muss am Ende mein return key = funktion sein damit ich es dann printen kann


total = 0; # This is global variable.

# Function definition is here
def sum2( arg1, arg2 ):
    # Add both the parameters and return them."
    total = arg1 + arg2; # Here total is local variable.
    print("Inside the function local total : ", total)
    return total;

# Now you can call sum function
sum2( 10, 20 )		#wenn ich total=sums2(10,20) schreibe verändere ich auch das äußere total
print("Outside the function global total : ", total)




#return how many bets he won
