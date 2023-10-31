#Assignment 1 dice throw
import random;
dice = 0;
i = 0;
rollTracker=[];
while (dice != 6):
    dice = random.randrange(1,7)
    i = i+1
    print(i, dice,'(ಥ﹏ಥ)')
    rollTracker.append(dice)   
print(f"It took {i} throws to get a 6 (*^‿^*)")
print("All the throws were",rollTracker)

