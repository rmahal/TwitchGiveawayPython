import urllib
import json
from random import randint
import random
from distutils.core import setup


host = raw_input("What is your twitch channel? ")
print(host)
url = "https://tmi.twitch.tv/group/user/"+host+"/chatters"


programstate = True
while (programstate == True):
    print ("\n"),
    response = urllib.urlopen(url)
    data = json.loads(response.read().decode('utf-8'))
    mods = data['chatters']['moderators']
    staff = data['chatters']['staff']
    admins = data['chatters']['admins']
    globalmods = data['chatters']['global_mods']
    viewers = data['chatters']['viewers']



    chatters = []
    viewernumlist = []



    for x in mods:
        chatters.append(x)
    for x in staff:
        chatters.append(x)
    for x in admins:
        chatters.append(x)
    for x in globalmods:
        chatters.append(x)
    for x in viewers:
        chatters.append(x)

    viewernumlist = chatters

    if(len(chatters) == 0):
        print ("There are currently no viewers please try again later!"),
        programstate = False
    else:
        shfl = random.randint(0,9)
        counter = 0
    
        while(counter<shfl):
            random.shuffle(chatters)
            counter= counter+1


        winningnum = random.randint(0,(len(chatters)-1))
        winner = chatters[winningnum]

        while (str(winner)== host or str(winner)=="nightbot"):
            print ("\nCOLUSION, HOST INELIGIBLE...PICKING AGAIN!\n"),
            winningnum = random.randint(0,(len(chatters)-1))
            winner = chatters[winningnum]

    

        print "\n\nCurrently",
        print len(chatters),
        print "viewers.\n",
        print "Winner is:",str(winner)," viewer #",winningnum+1,"\n\n",

        userchoice = raw_input("\nWould you like to reroll? Please type 'Yes' to continue or 'No' to quit: ")
           
        if(userchoice == "no" or userchoice == "No" or userchoice == "nO" or userchoice == "NO"):
            print ("\nThank you, Goodbye!"),
            programstate = False
        else:
            print ("\nREROLLING!"),
