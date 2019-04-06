def kitchen(): 
    print "In the Kitchen you see a Fridge, Stove, and Table ... "
    bool = True
    while True:
        inputVal = input("Your choices are:\n1.Fridge\n2.Stove\n3.Table\n4.Return to Hallway\nSelect choice: ")
        if inputVal==1:
            print "       ___________,_____"
            print "      |     |  #  |=====|"
            print "      |     | (_) |=====|"
            print "      |> _  |_____|=====|"
            print "      | [_] |     |     |"
            print "      |     |_____|=====|"
            print "      |     |     |_____|"
            print "      |   ] |_____|     |"
            print "      |     |_____|=====|"
            print "      |     | ___ |_____|"
            print "      |>    |[___]|     |"
            print "      |     |[___]|=====|"
            print "      |_____|=====|_____|"
            print "\nYou look at the fridge, you stomach grumbles ... you are hungry"
        elif inputVal==2:
            if bool:
                print "                 _.-------------."
                print "             .-''            .;'|"
                print "            ;==============;+'  |"
                print "            |              |    |"
                print "            | (} (} {) (}  |    |"
                print "            |              |    | "
                print "            | .==========. |    |"
                print "            | | _ .''+_/)| |    |"
                print "            | |( \(  (`( | |    |  "
                print "            | | \- `.  -)| |    |"
                print "            | | ( (  _  )| |    |"
                print "            | |  `--' `' | |    ;"
                print "            | `----------' |  .'"
                print "            |              |.'"
                print "            `--------------'  "
                print "\nYou look at the stove, there is a letter sitting on top ..."
                letter(letterCount)
                global letterCount
                letterCount += 1
                bool = False
            else: print "\nYou already read this letter ..."

#add in stuff for reading letter twice etc ... ADD COUNTER, for first letter, write some specific statements etc
        elif inputVal==3:
            print "                     ,%;,"
            print "                     ,%%,"
            print "        ______________)(______________"
            print "       /    \(__)    (__)             \ "
            print "      /________________________________\ "
            print "         \ \  / /            \ \  / /"
            print "          \ \/ /              \ \/ /"
            print "          _\/ /________________\ \/_"
            print "         [_/o/__________________\o\_]"
            print "          / /\ \              / /\ \ "
            print "         /_/  \_\            /_/  \_\ "
            print "\nYou look at the table, yesterdays dirty dishes are left. Sophia has been rather absent recently ..."
        elif inputVal==4:
            return
        else:
 	        print"\nInvalid choice\n"

def garage():
    print "In the Garage you see Sophia's car is missing, the concrete is cool on your feet, where did she go?"
    while True:
        inputVal = input("Your choices are:\n1.Look through the window\n2.Return to Hallway\nSelect choice: ")
        if inputVal==1:
            print "You look through the window, there are no cars in sight. It is a sunny and beautiful day ..."
            print "you wish you could go outside for a bit ..."
        elif inputVal==2:
            return
        else:
            print"\nInvalid choice\n"

def window():
    global boolGlobal
    if boolGlobal:
        print "    o=(=(=(=(=(=(=)=)=)=)=o"
        print "     !-'-'-'-/_\-'-'-'-! "
        print "     ! !  , /___\`  ! !!"
        print "     !!! , /  |  \`  ! !"
        print "     !!  ,|___|___`  !!!"
        print "     !_,| |_______|` `_!"
        print "     !-`| |       | |,-!"
        print "     !!!! |       | ! !!"
        print "     !!!! |       | !!!!"
        print "     !!!!_|_______|_!!!!"
        print "     !!!!___________!!!! "
        print "     !!!!           !!!!  "
        print "     !!!!           !!!!"
        print "You peek through the window, a bird flys by and you are distracted for a period of time ... "
        boolGlobal = False
    else: print "You peek through the window again, sadly there's no bird this time ..."

def livingRoom():
    print "In the living room and see a TV, Couch, and Coffee Table"
    bool = True
    while True:
        inputVal = input("Your choices are:\n1.TV\n2.Couch\n3.Coffee Table\n4.Return to Hallway\nSelect choice: ")
        if inputVal==1:
            print "      \\     // "
            print "       \\   //"
            print "        \\ // "
            print "       /~~~~~\ "
            print ",-------------------,"
            print "| ,---------------, |"
            print "| |               | |"
            print "| |               | |"
            print "| |               | |"
            print "| |               | |"
            print "| |               | |"
            print "|___________________|"
            print "|___________________|"
            print "The TV is on, soothing music is playing."
        elif inputVal==2:
            if bool:
                print "     .------------------."
                print "     | . . . . . . . . .|"
                print "     | .'.'.'.'.'.'.'.'.|"
                print "    ()______ ____ ______()"
                print "    ||______I____I______||"
                print "    ||__________________||"
                print "     W                  W "
                print "You see a letter stuffed between the cushions... "
                letter(letterCount)
                global letterCount
                letterCount += 1
                bool = False
            else: print "You see the couch with the letter you already read ..."
        elif inputVal==3:
            print "        _______________________"
            print "       /                        \ "
            print "      /__________________________\ "
            print "      [__________________________]"
            print "       | |                    | |"
            print "       | |                    | |"
            print "        w                      w"
            print "You look on the coffee table, there is a half finished cup of tea ... Sophia always finishes her tea"
        elif inputVal==4:
            return
        else:
            print"\nInvalid choice\n"

def bathroom():
    print "In the bathroom you see a Sink and Bathtub. Sophia didn't drain her last bath ... lazy"
    bool = True
    while True:
        inputVal = input("Your choices are:\n1.Sink\n2.Bathtub\n3.Return to Hallway\nSelect choice: ")
        if inputVal==1:
            print "              _    __    _ "
            print "             /_\  /  \  /_\  "
            print "             =|= | // | =|=  "
            print "              !   \__/   !  "
            print "                    _       "
            print "                   //'     "
            print "               __T_||_T__  "
            print "              [__________] "
            print "               \_      _/ "
            print "                 \    / "
            print "                  |  | "
            print "                  |  | "
            print " _________________|  |________"
            print "                 (____)      "
            print "               .;;;;;;;;.  "
            print "              :;;;;;;;;;;:"
            print "               '::::::::'"
            print "You look at the sink, and see your reflection in the mirror. You look cute today :3"
        elif inputVal==2:
            if bool:
                print "Oo (--------------------------)"
                print "    \                        /    o"
                print "     \                      /    _   ."
                print "      \          _         /    (_)"
                print "   o  `-. .----<(o)_--. .-'"
                print "   ----(_/------(_<_/--\_)---"

                print "You look at the bathtub and dip your foot in the water, it is cold and you are now upset"
                print "to the side of the tub you see a letter ... "
                letter(letterCount)
                global letterCount
                letterCount += 1
                bool = False
            else: 
                print "You look at the bathtub and dip your foot in the water, it is cold and you are now upset"
                print "to the side of the tub you see the letter you already read ..."
        elif inputVal==3:
            return
        else:
 	        print"\nInvalid choice\n"

def bedroom():
    print "          !__________!    .    _______"
    print "          |____  ____|   /_\   |__*__|"
    print "          {____}{____}  __|__  |__*__|"
    print " _________%%%%%%%%%%%%__|_*_|__|__*__|"
    print "         %%%%%%%%%%%%%% |   |  |/   \|"
    print "        %%%%%%%%%%%%%%%%"
    print "       %%%%%%%%%%%%%%%%%%"
    print "      %%%%%%%%%%%%%%%%%%%%"
    print "     /||||||||||||||||||||\ "
    print "     |||||||||||||||||||||| "


    print "In the bedroom you see a Bed, Dresser, and Nightstand. It's chilly in here."
    bool = True
    while True:
        inputVal = input("Your choices are:\n1.Bed\n2.Dresser\n3.Nightstand\n4.Return to Hallway\nSelect choice: ")
        if inputVal==1:
	        print "You look at the bed, it is made nice and neat. You have an urge to get under the covers for a bit."
           # print "so you do ..."
        elif inputVal==2:
            if bool:
                print "You look at the dressser, there is a letter ..."
                letter(letterCount)
                global letterCount
                letterCount += 1
                bool = False
            else: print "You look at the dresser, and find the letter that you've a letter already read ..."
        elif inputVal==3:
            print "You look at the nightstand, there is a cute picture of you and Sophia."
            print "it fills you with love"
        elif inputVal==4:
            return
        else:
	        print"\nInvalid choice\n"
	
def energyBar():
    global energy
    print "Energy Level ",energy,"%"

def hallway():
    
    while True:
        print "\nYou are in the hallway\n"
        energyBar()
        global energy
        if energy == 0:
            print "\nSimon closes his eyes and begins to drift away ... his eyes do not open again.\n"     
            return
        print "Your choices are:\n1.Bedroom\n2.Bathroom\n3.Kitchen\n4.Garage\n5.Window\n6.Living Room\n7.Nap"
        inputVal = input("\nEnter your choice: ")
        if inputVal==1:
	        bedroom()
        elif inputVal==2:
	        bathroom()
        elif inputVal==3:
	        kitchen()
        elif inputVal==4:
	        garage()
        elif inputVal==5:
	        window()
        elif inputVal==6:
	        livingRoom()
        elif inputVal==7:
	        nap()
        elif inputVal==0:
            return
        else:
	        print "\nInvalid entry\n"
        energy -= 10

def nap():
   global energy
   print "Napping..."
   energy = 110

def letter(letter): 
    if letter == 1:
        print "Dear Sophia,\nI had an amazing time with you today. I am so glad that we were\nable to connect. I would love nothing more than to see you again in the\nnear furture ...\nWarmly,\nKarl"
        print "*KARL! Who is this KARL. I must find out more information ... but why would Sophia hide\nthis from me?*"
    elif letter == 2:
        print "Dearest Sophia,\nI am so happy that we were able to meet up again! I am so grateful for your presence.\nYou are the love that came without warning; you had my heart before I could say no!\nLove,\nKarl"
        print "*They met up again! My hear is breaking ... Sophia ...*"
    elif letter == 3:
        print "Sophia!\nNo mountain, nor sea, no thing of this world could keep us apart, because this\nis not my world. You are! I think it is finally time to say, I LOVE YOU!\nLove,\nKarl <3"
        print "*I ... I cant belive this. Sophia ... my love ...*"
    elif letter == 4:
        print "My Love!\nYou are someone who makes love feel easy. I cannot express my deepest emotions in\nwords. You are everything to me. Being in love is a strange thing, my thoughts constantly\ndrift towards you. My stomach is in a constant state of butterflies. I have completely\nfallen for you. Everything you do, everything you say, everything you are. You are my\nfirst thought in the morning and the last thought I have before bed. And every thought\ninbetween ... you're there too.\nCan't wait to come by later,\nXOXO Karl"
        print"*This is the final straw! The second she gets home she will hear what I have to think!\nHow dare she ... the bond we have ...*"


print"-----------------------------------------"
print"            Wake up Simon"
print"-----------------------------------------"
print"    you wake up in the hallway. why did you fall asleep here? you stand up and stretch."
print"Where is Sophia? you need to find out where she went. better investigate.              "
energy=100
letterCount = 1
boolGlobal = True
hallway()





