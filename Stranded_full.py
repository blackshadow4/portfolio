GameOn = True

while GameOn:
    print ("You wake up dased. You can't remember much but . . . you remember a fight?")
    print ("You appear to be in some kind of cave. The walls are made of orange stone")
    print ("and the floor is covered in a thin layer of sand. What do you do?")
    print ("1. Try to survive in the cave")
    print ("2. Try to survive in the desert wastland outside")
    option1 = int(input("Enter 1 or 2"))

    if option1 == 1:
        print ("you rest your back on the cave wall and settle in")
        print ("  ")
        print ("NIGHT FALLS")
        print ("  ")
        WrongNight = True
        while WrongNight:
            print ("as you sit there in the blue darkness you think about what you could do")
            print ("you deside to . . .")
            NC = True
            while NC:
                print ("1. Star gaze")
                print ("2. Explore the cave")
                print ("3. Sleep")
                NightChoice = int(input("Enter 1, 2, or 3"))

                if NightChoice == 1:
                    print ("this is nice")
                    print ("  ")
                    print (". . .")
                    print ("don't the stars just seem to go on forever")
                    print ("the vast skyes remind you of home")
                    print ("  ")
                    print ("your chest starts to feel hollow")
                    print ("  ")
                    print ("  ")
                    print (" T^T ")
                    print ("  ")
                    print ("  ")
                    print ("go in?")
                    SadStars = int(input("1. Ya, 2. no, I'm fine"))
                    if SadStars == 1:
                        print ("you go back into the now much more present emptyness of the cave")
                        print ("what now?")
                        NC = True
                    elif SadStars == 2:
                        print ("you fall aseep outside")
                        print ("hugging yourself under the stars")
                        NC = False
                    WrongNight = False

                elif NightChoice == 2:
                    path = True
                    while path:
                        print ("  ")
                        print ("you go further into the cave")
                        print ("you come to a split")
                        print ("from the left split you feel friged air")
                        print ("from the right split you feel warm air")
                        ImBack = True
                        while ImBack:
                        RoadSplit = int(input("1. Left or 2. Right"))
                        if RoadSplit == 1:
                            print ("  ")
                            print ("As you travel down the dark tunnel you hear a drip, drip,")
                            print ("drip echoing off the walls")
                            print ("  ")
                            print ("you found a cave lake!!!")
                            print ("  ")
                            print ("in the cave lake there are small fish")
                            print ("MEAT!")
                            print ("WATER!")
                            print ("  ")
                            print ("do you want to chack out the other tunnel?")
                            tunnelCheck = int(input("1. ya, 2. no, I want to go back to the front of the cave"))

                            if tunnelCheck == 1:
                                print ("you walk back up the dark tunnel now satisfide by your prise")
                                print ("  ")
                                ImBack = True
                                path = False
                            elif tunnelCheck == 2:
                                print ("you go back to the front of the cave, now layden with you prise")
                                ImBack = False
                                path = False

                        elif RoadSplit == 2:
                            print ("As you go further into the dark tunnel the warm air begins to smell sweet")
                            print ("  ")
                            print ("after walking for a while you come to a room lit by byoluminecent worms!")
                            print ("Plants are growing everywhere! all over the walls and floor!")
                            print ("Fuit baring plants!!")
                            print ("  ")
                            print ("do you want to chack out the other tunnel?")
                            tunnelCheck = int(input("1. ya, 2. no, I want to go back to the front of the cave"))

                            if tunnelCheck == 1:
                                print ("you walk back up the dark tunnel now satisfide by your prise")
                                print ("  ")
                                ImBack = True
                                path = False
                            elif tunnelCheck == 2:
                                print ("you go back to the front of the cave, now layden with you prise")
                                ImBack = False
                                path = False

                        print ("you now live ")

                        else:
                            print ("there are litteraly two numbers to choose from,")
                            print ("this is not that hard")
                            print ("  ")
                            path = True
                            WrongNight = False

                elif NightChoice == 3:
                    print ("  ")
                    print ("you go to sleep")
                    print ("  ")
                    print (" .*:.C'*.. ")
                    print ("  ")
                    print ("You had a nice night")
                    print ("you're pretty hungry, would you like to look around the cave")
                    WrongNight = False
                else:
                    print ("*sigh*")
                    print ("alright lets try this again")
                    print ("  ")

    elif option1 == 2:
        print ("")
        print ("The sun is scortching")
        print("You start to feel thitsty")
        water_yes_no = input("If you want to look for water type 'yes' if not type 'no'to keep going ")
        if water_yes_no == "yes":
            print("You can either 'dig' in the sand or... you see a 'tree' in the distance")
            tree_or_dig = input("Type 'dig' to go in the sand or type 'tree' to see what the tree has to offer")
            if tree_or_dig == "tree":
                print("Theres nothing here")
                print("You spent a day and a half walking twards a mirage")
                print("You colapse and die of dehydration")
                print("THE END")
                #END GAME
            elif tree_or_dig =="dig":
                print ("you come across a burrowing beetle")
                print ("it bites you")
                print ("DAMAGE -5!!")
                eat_or_slap = input("Type 'eat' to eat the beetle or type 'slap' to slap it")
                if eat_or_slap == "eat":
                    print("its nutritios and full of water, but its poisionous!")
                    print("you feel very sick")
                    print("you die a day later")
                    print("THE END")
                    #END GAME
                elif eat_or_slap =="slap":
                    print("the bettle runs off")
                    print("you hit wet sand")
                    print("WATER!!!!")
                    print("you drink the water but do it too quickly")
                    print("you choke on sand...")
                    print("you dont have enough strenth to save youself")
                    print("you die of aspiixiation")
                    print("THE END")
                    #END GAME
        elif water_yes_no =="no":
            #KATHERINE
            print ("You come across a snake!")
            print("1. Fight")
            print("2. Back away")
            option =int(input("Enter 1 or 2"))
            if option==1:
                print("You punch that snake in the face!")
                print("He strikes you back in the arm!")
                print("You break his neck!!!")
                print("Well I guess you have a nice dinner now.")
                print("What now?")
                print("1.Accept your fate")
                print("2.Tie off the bite")
                option3 =int(input("Enter 1 or 2"))
                if option3==2:
                    print("You stopped the venom flow! But now you don't have any pants")
                    print("You last several days with your arm getting progressively more purple")
                    print("When you're certain you can't go on any further, you see buildings in the distance")
                    print("You make it to civilization")
                    print("You live! YAY! :DDDDDDDD")
                    print("~THE END~")
                if option3==1:
                    print("You accept the end..")
                    print("You lie down in the sand...")
                    print("You die about an hour later....")
                    print("~THE END~ :,,,(")
            elif option==2:
                print("You start to back away but the snake yells something at you?")
                print("It says 'No wait!! Follow me'")
                print("WTH it's a snake??")
                print("1. Run away")
                print("2. Just go with it")
                option2 =int(input("Enter 1 or 2"))
                if option2==2:
                    print("You decide to follow the snake. It feels like hours, but eventually you reach an oasis!")
                    print("You spend the rest of your days in the desert with the snake as your companion :D")
                    print("...")
                    print("is this for real")
                    print("~THE END~")
            #the next code is for later Im starting at run diamond
        elif option2 ==1:
            print("night falls")
            print("youre hopelessly lost")
            print("you encounter a cyote")
            cyote_choice = input("Type 'run' to run away, type 'attack' to attack it, type 'talk' to talk to the cyote, type 'lay' to lay down")
            if cyote_choice =="run":
                print("You get away but you collaps from exhaustion")
                print("You pass out")
                print("You dont wake up...")
                print("THE END")
                #END GAME
            elif cyote_choice =="attack":
                print("who do you think you are?")
                print("That cyote beats your ass!")
                print("The pups will eat well tonight....")
                print("THE END")
                #END GAME
            elif cyote_choice =="talk":
                print("valient effort")
                print("but you've lost it now")
                print("probably the heat...")
                print("the cyote growls")
                talk_or_run = input("Type 'talk' to try and reason with they cyote again, or type 'run' to get away")
                if talk_or_run == "talk":
                    print("Cyote: Hello Human")
                    print("HOLY **** IT WORKED!!!")
                    print("You go home with the cyote and live the rest of your days with your new friend")
                    print("nice job")
                    print("THE END")
                    #END GAME
                elif talk_or_run =="run":
                    print("You get away but you collaps from exhaustion")
                    print("You pass out")
                    print("You dont wake up...")
                    print("THE END")
                    #END GAME
            elif cyote_choice == "lay":
                print("The cyote sniffs you")
                print("it licks your face")
                print("it bends down")
                print("its breath tickles your ear")
                print("Cyote:Sorry man but I really got to eat you")
                print("the cyote snaps your neck with its jaws")
                print("THE END")
                #GAME OVER
    else:
        print ("  ")
        print ("comeon man, if you don't follow directions than this is not gonna work")
        print ("lets try this again")
        print ("  ")
