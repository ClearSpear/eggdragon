#!/bin/usr/env python3

import time
import os
import random
import sys

def titleScreen():
    print("Welcome! Don't type anything quite yet please.")
    time.sleep(2)
    print("This is the world of Liera,")
    time.sleep(1)
    print("a world with dragons and fantastical flowers and squirrel carcasses,")
    time.sleep(1)
    print("and you inhabit it.")
    time.sleep(2)
    print("Last week, you visited the Noraf woods")
    time.sleep(1)
    print("and found a dragon egg!")
    time.sleep(2)
    print("That was the beginning.")
    time.sleep(2)
    print("Maybe you can get to a full dragon at 50 days old.")
    time.sleep(1)
    print("But anyway..")
    time.sleep(2)
    print("The rest of this story is up to you.")
    print("")
    time.sleep(2)
    txt = raw_input("Press enter to continue.")
    return

def eggHatching():
    os.system('CLS')
    print(""" 




      _-- _
     /     |
    / ##    |
   |  #      |
 %  \       /
_|*+_\_____/_^/!_""")
    time.sleep(.5)
    os.system('CLS')
    print("""




      _-- _
    /     |
   / ##    |
  |  #      |
 %  \       /
_|*+_\_____/_^/!_""")
    time.sleep(.2)
    os.system('CLS')
    print(""" 




      _-- _
     /     |
    / ##    |
   |  #      |
 %  \       /
_|*+_\_____/_^/!_""")
    time.sleep(.2)
    os.system('CLS')
    print(""" 




       _-- _
      /     |
    / ##    |
    |  #      |
  %  \       /
_|*+_\_____/_^/!_""")
    time.sleep(.2)
    os.system('CLS')
    print(""" 




      _-- _
     /     |
    / ##    |
   |  #      |
 %  \       /
_|*+_\_____/_^/!_""")
    time.sleep(1.5)
    os.system('CLS')
    print("""


      /\_/|
  /\  |o o|  /|
.,  / _/  \ \  ,.|
 # / /     \,
    / ##    \,
   |  #      |
 %  \       /
_|*+_\_____/_^/!_""")
    time.sleep(.1)
    os.system('CLS')
    print("""
      /\_/|
  /\  |o o|  /|
 /  \,\<">/ /  |
/ .__~_)-( ~__, |
.,  / _/  \ \  ,.|
 # / /     \,
    / ##    \,
   |  #      |
 %  \       /
_|*+_\_____/_^/!_""")    
    time.sleep(2)
    txt = raw_input("""

Press enter to continue continuing.""")
    return

def gameIntro():
    txt = raw_input("Your dragon has hatched!")
    time.sleep(.2)
    txt = raw_input("It's revitalized from just being born, but soon it will get hungry and tired and unhappy, and it may even get sick at some point.")
    time.sleep(.2)
    txt = raw_input("You've found a nice den for it, and for now it's there, waiting for you.") 
    time.sleep(.2)
    txt = raw_input("To start up, enter 'help' to see what you can do.")
    time.sleep(.2)
    txt = raw_input("Good luck!")
    time.sleep(.2)
    return

def reEntry():
    txt = raw_input("""Welcome back!
We thought you were gone forever. =P 

Your dragon is happy to see you. 
        , ,
    ,  /|_|\.  ,
   /{ { 0 0 } }\. /|
  //\  \   /  /\|{{
 //  '-/'-'\-'  \|))
 |(   | (=) |   )|(
 \    (\|=//)    /)
  \|\|\/"'"\/|/|/

""")
    txt = raw_input("Remember you can enter 'help' at any time if you need it.")
    return

def happyEnding():
    os.system('CLS')
    txt = raw_input("Your dragon is at ... hold up...")
    txt = raw_input("Your dragon is 50 days old!")
    print("")
    checkDragon(dragonStat)
    print("")
    txt = raw_input("Wow! I can't believe you- I mean, I knew you could do it. Good job.")
    txt = raw_input("Yes.")
    txt = raw_input("Here he is, what a beaut.")
    txt = raw_input("""
            ,'\   |\.
           / /.:  ;;
          / :'|| //
         (| | || //
         / ||,;'-.._
        : ,;,`';:.--`
        |:|'`-(\.
        ::: \-'\`'
         \.\ \,-`.
          `'\ `.,-'-._      ,-._
   ,-.       \  `.,-' `-.  / ,..`.
  / ,.`.      `.  \ _.-' \.,: ``\ \.
 / / :..`-'''``-)  `.   _.:''  ''\ \.
: :  '' `-..''`/    |-''  |''  '' \ \.
| |  ''   ''  :     |__..-;''  ''  : :
| |  ''   ''  |     ;    / ''  ''  | |
| |  ''   ''  ;    /--../_ ''_ '' _| |
| |  ''  _;:_/    :._  /-.'',-.'',-. |
: :  '',;'`;/     |_ ,(             \|
 \ \  \(   /\     :,'  \.
  \ \.'/  : /    ,)    /
   \ ':   ':    / \   :
    `.\    :   :\  \  |
            \  | `. \ |..-_
         SSt ) |.  `/___-.-'
           ,'  -.'.  `. `'        _,)
           \.\('.\ `._ `-..___..-','
              `'      ``-..___..-'
""")
    txt = raw_input("Well that's it!")
    txt = raw_input("Thanks for playing!")
    txt = raw_input("All ascii art credit goes to the internet artists out there. And I'd like to thank my compsci teachers Mr. Q and Dr. Morrison for teaching me how to use a computer because wow it's hard. (No sarcasm.)")
    txt = raw_input("Okay.")
    txt = raw_input("You can leave now...")
    txt = raw_input("kbai")
    return

def deathScene():
    txt = raw_input("Your dragon is at 0 health.")
    print("")
    checkDragon(dragonStat)
    print("")
    txt = raw_input("It's uh...")
    txt = raw_input("""
                                ____
         ,.-''''-,__,..---'''```    ``''-.
        //      '   `.                    `,
       7;                         )         .
      Y    \  /                  /           L,
      : \.  \|                 ,`            | `'.
  ,.-'^, \.'`',    (           ;             ;    `,
 //`_),.\|\)_ .\   /          ,A          ._,^      \.
 L\)  ,+`[  x\ \.-`''--......-__'.  _,       `\.     )Y
 _,--`   \   )`.`,           // ````          / )_.-' |
//./`_)'` `''-. `/    _,.......----------'"'"'``      /
\.)\)          `"   +'  ________                   _,`
 `` `             ,`,'``         ```````'""'""'"'``
                  |7  sk
                   \_,

dead. """)
    txt = raw_input("Oh well...")
    txt = raw_input("Try again?")
    return

def dayPass(dragonStat):
    dragonStat[0] += 1
    dragonStat[1] += 1
    dragonStat[3] += -5
    if dragonStat[6] == 0:
        dragonStat[4] += 25
        dragonStat[5] += -5
        if random.randint(0,20) < 2: 
            if dragonStat[2] == 0:
                dragonStat[2] = 1
                print("Your dragon is sick!")
        if random.randint(0,20) < 5:
            if dragonStat[2] == 1:
                dragonStat[2] = 0
                print("Your dragon recovered from being sick.")
    if dragonStat[6] == 1:
        dragonStat[4] += -10
        dragonStat[5] += 5
        if random.randint(0,20) < 5: 
            if dragonStat[2] == 0:    
                dragonStat[2] = 1
                print("Your dragon is sick!")
        if random.randint(0,20) < 2:
            if dragonStat[2] == 1:    
                dragonStat[2] = 0
                print("Your dragon recovered from being sick.")
    if dragonStat[2] == 1:
        dragonStat[3] += -10
        dragonStat[4] += -10
        dragonStat[5] += -10
    if dragonStat[3] <= 0:    
        print("Your dragon is famished.")
        dragonStat[1] += -10
    if dragonStat[4] <= 0:    
        print("Your dragon is exhausted.")
        dragonStat[1] += -25
    if dragonStat[5] <= 0:     
        print("Your dragon isn't happy.")
        dragonStat[1] += -5
    if dragonStat[1] <=0:    
        print("Your dragon has died.")
        dragonStat[7] = 1
        return dragonStat
    if dragonStat[1] > dragonStat[0] + 1:    
        dragonStat[1] = dragonStat[0] + 1
    if dragonStat[3] > 100:    
        dragonStat[3] = 100
    if dragonStat[3] < 0:    
        dragonStat[3] = 0
    if dragonStat[4] > 100:    
        dragonStat[4] = 100
    if dragonStat[4] < 0:    
        dragonStat[4] = 0
    if dragonStat[5] > 100:    
        dragonStat[5] = 100
    if dragonStat[5] < 0:     
        dragonStat[5] = 0
    print("Your dragon is at " + str(dragonStat[1]) + " health.")
    if dragonStat[0] == 25:
        print("Hey you're halfway there! This game really DRAGs ON doesn't it? Ahahahahaha... okay Amanda.")
    return dragonStat

def moveToDen(dragonStat):
    if dragonStat[6] == 1:
        dragonStat[6] = 0
        print("Your dragon spent the day traveling to the den.")
        dayPass(dragonStat)
    elif dragonStat[6] == 0:
        print("You are already in the den.")
    else:
        print("error")
    return dragonStat

def moveToWoods(dragonStat):
    if dragonStat[6] == 0: 
        dragonStat[6] = 1
        print("Your dragon spent the day traveling to the woods.")
        dayPass(dragonStat)
    elif dragonStat[6] == 1:
        print("You are already in the woods.") 
    else:
        print("error")
    return dragonStat

def forage(dragonStat):
    if dragonStat[6] == 1:
        times = random.randint(0,3)
        print("Your dragon foraged in the woods all day and found " + str(times) + " items.")
        while times > 0:
            randomItem = random.randint(8,17)
            dragonStat[randomItem] += 1
            if randomItem == 8:
                print("a bluebell petal")
            if randomItem == 9:
                print("a crisp leaf")
            if randomItem == 10:
                print("a water droplet")
            if randomItem == 11:
                print("a crystal sunflower")
            if randomItem == 12:
                print("a squirrel carcass")
            if randomItem == 13:
                print("an apple")
            if randomItem == 14:
                print("a fish")
            if randomItem == 15:
                print("a robin egg")
            if randomItem == 16:
                print("a coffee bean")
            if randomItem == 17:
                print("a mint leaf")
            times = times - 1
        dayPass(dragonStat)
    else:
        print("There is nothing to forage for in the den.")
    return dragonStat

def stay(dragonStat):
    if dragonStat[6] == 0:
        dayPass(dragonStat)
    else:
        print("You're in the woods. Do something.")
    return dragonStat


def bluebellPetal(dragonStat):
    if dragonStat[8] > 0:
        dragonStat[1] += 2
        dragonStat[8] += -1
        print("Your dragon consumed 1 bluebell petal.")
    else:
        print("You don't have any of this item.")
    return dragonStat

def crispLeaf(dragonStat):
    if dragonStat[9] > 0:
        dragonStat[1] += 2
        dragonStat[9] += -1
        print("Your dragon consumed 1 crisp leaf.")
    else:
        print("You don't have any of this item.")
    return dragonStat

def waterDroplet(dragonStat):
    if dragonStat[10] > 0:
        dragonStat[1] += 2
        dragonStat[10] += -1
        print("Your dragon consumed 1 water droplet.")
    else:
        print("You don't have any of this item.")
    return dragonStat

def crystalSunflower(dragonStat):
    if dragonStat[11] > 0:
        dragonStat[2] = 0 
        dragonStat[11] += -1
        print("Your dragon consumed 1 crystal sunflower.")
    else:
        print("You don't have any of this item.")
    return dragonStat

def squirrelCarcass(dragonStat): 
    if dragonStat[12] > 0:
        print("Your dragon consumed 1 squirrel carcass.")
        dragonStat[3] += 10
        if random.randint(1,20) == 1 and dragonStat[2] == 0:
            dragonStat[2] = 1
            print("Your dragon got sick from eating that!")
        dragonStat[12] += -1
    else:
        print("You don't have any of this item.")
    return dragonStat

def apple(dragonStat):
    if dragonStat[13] > 0:
        print("Your dragon consumed 1 apple.")
        dragonStat[3] += 5
        dragonStat[5] += 1
        dragonStat[13] += -1
    else:
        print("You don't have any of this item.")
    return dragonStat

def fish(dragonStat):
    if dragonStat[14] > 0:
        print("Your dragon consumed 1 fish.")
        dragonStat[3] += 20
        dragonStat[5] += 5
        dragonStat[14] += -1
    else:
        print("You don't have any of this item.")
    return dragonStat

def robinEgg(dragonStat):
    if dragonStat[15] > 0:
        print("Your dragon consumed 1 robin egg.")
        dragonStat[3] += 15
        dragonStat[5] += 5
        dragonStat[15] += -1
    else:
        print("You don't have any of this item.")
    return dragonStat

def coffeeBean(dragonStat):
    if dragonStat[16] > 0: 
        print("Your dragon consumed 1 coffee bean.")
        dragonStat[4] += 10
        dragonStat[16] += -1
    else:
        print("You don't have any of this item.")
    return dragonStat

def mintLeaf(dragonStat):
    if dragonStat[17] > 0:
        print("Your dragon consumed 1 mint leaf.")
        dragonStat[5] += 10
        dragonStat[17] += -1
    else:
        print("You don't have any of this item.")
    return dragonStat


def txtToGame(dragonLocation):
    os.system('CLS')
    saveFile = open(dragonLocation, "r")
    workedSaveFile = ""
    nameLines = []
    dragonStat = []

    #player1 = input("Hello. Your name is? ")
    
    for line in saveFile:
        workedSaveFile = workedSaveFile + line
    workedSaveFile = workedSaveFile.split("""
""")

    #for term in workedSaveFile:
    #    if player1 in term:
    #        print(term)
    #        print("in file")

    dragonStatStr = workedSaveFile[-2]
    
    for word in workedSaveFile:
        if 'name' in word:
            nameLines += [word]
    print("Hello, " + nameLines[-1][5:] + ". :3")
    
    saveFile.close()
    dragonStatStrType = dragonStatStr.split(',')
    for word in dragonStatStrType: 
        dragonStat = dragonStat + [int(word)]
    return dragonStat

def gameToTxt(dragonLocation):
    dragonStatStrType = []
    for int in dragonStat:
        dragonStatStrType += [str(int)]
    newSaveData = ",".join(dragonStatStrType)
    saveFile = open(dragonLocation, "a")
    saveFile.write(newSaveData + """
""")
    saveFile.close()
    print("Save complete.")
    print("New save data: " + newSaveData)
    return


def itemList():
    print("""
There was an old etching in the wall of the den. It describes the flora and fauna of the woods nearby. 

Bluebell petals add 2 to health. 
Crisp leaves add 2 to health. 
Water droplets add 2 to health. 
Crystal sunflowers cure sickness. 
Squirrel carcasses add 10 to hunger but may make your dragon sick. 
Apples add 5 to hunger and make your dragon slightly happier. 
Fish add 20 to hunger and make your dragon happier. 
Robin eggs add 15 to hunger and make your dragon happier. 
Coffee beans add 10 to rest. 
Mint leaves add 10 to happiness. 
""")
    return

def checkDragon(dragonStat):
    print("Your dragon is " + str(dragonStat[0]) + " days old")
    print("Health: " + str(dragonStat[1]))
    if dragonStat[2] == 0:
        print("Sick: No")
    if dragonStat[2] == 1:
        print("Sick: Yes")
    print("Hunger: " + str(dragonStat[3]) + "%")
    print("Rest: " + str(dragonStat[4]) + "%")
    print("Happiness: " + str(dragonStat[5]) + "%")
    if dragonStat[6] == 0:
        print("Location: Den")
    if dragonStat[6] == 1:
        print("Location: Woods")
    if dragonStat[7] == 0:
        print("Dead: No")
    if dragonStat[7] == 1:
        print("Dead: Yes")
    print("Bluebell Petals: " + str(dragonStat[8]))
    print("Crisp leaves: " + str(dragonStat[9]))
    print("Water droplets: " + str(dragonStat[10]))
    print("Crystal sunflowers: " + str(dragonStat[11]))
    print("Squirrel carcasses: " + str(dragonStat[12]))
    print("Apples: " + str(dragonStat[13]))
    print("Fish: " + str(dragonStat[14]))
    print("Robin eggs: " + str(dragonStat[15]))
    print("Coffee beans: " + str(dragonStat[16]))
    print("Mint leaves: " + str(dragonStat[17]))
    return

def help():
    print("""Available actions:


These commands can be executed at any time.
 

Help
That is the command that printed this file.

Save
Save the current day's data to the file your dragon resides in. 

Quit
Saves the current day's data to the file your dragon resides in and then exits the program. 

Quit No Save
Exits the program WITHOUT SAVING. 


Check Dragon
This command will print the stats and inventory of your dragon. 

Check Item List
This command will print a list of all the items in the game and what they do. 

Consume ****
Replacing **** with an item name will instruct your dragon to consume one of that item. 


The commands below will take all day and cause a day to pass.


Move Den
Your dragon will travel back to the den and sleep there. You can only do this from the woods. 

Move Woods
Your dragon will travel back to the woods and sleep there. You can only do this from the den. 

Forage
Your dragon will spend the day foraging for items then sleep. You can only do this from the woods. 

Stay
Your dragon will spend the night in the den.


If your dragon gets sick, you have a better chance of recovering if you rest in the den.

GLHF
""")
    return

def checkEnd(dragonStat):
    if dragonStat[0] >= 50:
        happyEnding()
        return True
    if dragonStat[1] <= 0 or dragonStat[7] == 1:
        deathScene()
        return True
    return False


def UI():
    if checkEnd(dragonStat):
        sys.exit()

    command = raw_input("--> ")
    command = command.lower()
    
    if command == "help":
        help()
        UI()
    if command == "save":
        gameToTxt(dragonLocation)
        UI()
    if command == "quit":
        gameToTxt(dragonLocation)
        sys.exit()
    if command == "quit no save":
        sys.exit()
    if command == "check dragon":
        checkDragon(dragonStat)
        UI()
    if command == "check item list":
        itemList()
        UI()
    if command == "consume bluebell petal":
        bluebellPetal(dragonStat)
        UI()
    if command == "consume crisp leaf":
        crispLeaf(dragonStat)
        UI()
    if command == "consume water droplet":
        waterDroplet(dragonStat)
        UI()
    if command == "consume crystal sunflower":
        crystalSunflower(dragonStat)
        UI()
    if command == "consume squirrel carcass": 
        squirrelCarcass(dragonStat)
        UI()
    if command == "consume apple": 
        apple(dragonStat)
        UI()
    if command == "consume fish": 
        fish(dragonStat)
        UI()
    if command == "consume robin egg": 
        robinEgg(dragonStat)
        UI()
    if command == "consume coffee bean": 
        coffeeBean(dragonStat)
        UI()
    if command == "consume mint leaf": 
        mintLeaf(dragonStat)
        UI()
    if command == "move den":
        moveToDen(dragonStat)
        UI()
    if command == "move woods":
        moveToWoods(dragonStat)
        UI()
    if command == "forage":
        forage(dragonStat)
        UI()
    if command == "stay":
        stay(dragonStat)
        UI()
    else:
        UI()


dragonLocation = 'eggDragon.txt'
dragonStat = txtToGame(dragonLocation)

if dragonStat == [0,1,0,100,100,100,0,0,0,0,0,0,0,0,0,0,0,0]:
    titleScreen()
    eggHatching()
    gameIntro()
else: 
    reEntry()

UI()

