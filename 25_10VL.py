#userage = [21,25,23,22,26] #Eckige Klammern geben liste an
#print(userage[2:6]) #userage[Zahl] gibt die zahl aus der Liste dann an; negative Zahlen machen das es rückwärts gezähltwird
# wenn wir 2:4 machen, kriegen wir 2 Zahlen. Statesments wie 2:4 , :3 , und ::2 listen
#unterschiedlich auf

#	userAge = []
#	print(userAge)

# Ich kann nachdem ich eine leere Liste erstellt habe im Terminal unten
# sachen hinzufügen mit userAge.append(Zahl oder String)
# sachen löschen mit del userAge [Index nummer, also 1 oder 2 etc, die den Platz angeben)
# oder sachen ändern userAge[index] = veränderte Zahl also zum beispiel [0] = 69

#	fruit = ['Apple', 'banana','Mango','Peach']
    #morefruit = ['Kiwi','ananas']
    #print(len(fruit),len(morefruit))
    #allfruit = fruit + morefruit	# Minus funktioniert nicht
    #print (allfruit*3)		#man kann Listen zusammen addieren

# der code verändert sich immer mit Übungen, immer nochmal auf Folien nachchecken

#list1 = ['Apple', 'Banana', 1234]
#list2 = list1[:]			#list 2 würde sich normalerweise mitverändern, aber durch [:] nicht
#list2 = list1.copy()		# funktioniert auch mit de. Befehl.copy() 
#list1[-1] = 'Ananas'		# Das : sagt, dass liste 2 ein neues Objekt dann ist, bzw die kopie von liste1 nen 
#print (list1)
#print (list2)

#monthNames = ('Jan','feb','Mar','Apr','May','Jun','Jul','Sep','Oct','Nov','Dec')
#print (monthNames)
    # das ist ein tuple, erkennbar durch runde Klammern, weil dort sich der Inhalt nicht verändern lässt

#studentAge = {'Alice':22,'Bob':20,'Carl':'unknown'} #Dictionary erkennbar durch Klammer
#print(studentAge['Bob'])
#print (studentAge.keys()) 	#keys sind die Namen bzw die ersten Sachen, der name mit eienr Info
 #print (studentAge[1])		# geht nicht die line,
#studentAge['Bob'] = 24	# So kann man sachen in ein Dictionary adden, bzw zu ändern
#print (studentAge)

#studentAge = dict (Alice=22, Bob=20, Carl='unknown')	#So geht auch ein dictionary, IMO einfacher
#print(studentAge)

#myDict ={}
#myDict['apples']= 4
#myDict['toilet paper'] = 99
#myDict[0.815] = True
#myDict['Carl'] = 'unknown'
#print (myDict)
#x = myDict.get('toilet paper')
#print (x)
#print('apples'in myDict) # check if apples is in the list and says true
#print ('mango' in myDict)	# hier kommt obviously 0false
#print('apples' in myDict.values())	#false, weil, es nach dem value apple sucht. Apple ist ein key und kein Value.
#print (myDict.values())	#gibt mir nur die values der keys
#print ('unknown' in myDict.values()) # hier gehts weil unknown ein Value ist
#myDict.clear()
#print (myDict)

myDict1 = {1:'one',2:'two'}
myDict2 = {1:'one',3:'three'}

myDict1.update (myDict2)	# its adds the key 3 wihl value 'three' and checks which element is in it and which not and merch them
print(myDict1)
print(myDict2)

myDict1 = {1:'one',2:'two',3:'three'}
myDict2 = myDict1.copy()		#ohne das Copy sind beide Dict1/2 identisch
myDict1[3] = 'drei'		#Dozent empfehlt nicht die zahlen als keys zu nehmen, wei ldas verwirrend sein kann. Lieber Namen wie vorhin 'Alice' = 20
print(myDict1)
print(myDict2)











