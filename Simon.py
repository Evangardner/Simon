def kitchen(): 
    print "You enter the Kitchen and see a Fridge, Stove, and Table ... "
    while True:
        inputVal = input("Your choices are:\n1.Fridge\n2.Stove\n3.Table\n4.Return to Hallway\nSelect choice: ")

        if inputVal==1:
	        print "\nYou look at the fridge, you stomach grumbles ... you are hungry"
        elif inputVal==2:
            print "\nYou look at the stove, there is a letter sitting on top ..."
            #TODO Print letter 1
#add in stuff for reading letter twice etc ... ADD COUNTER, for first letter, write some specific statements etc
        elif inputVal==3:
            print "\nYou look at the table, yesterdays dirty dishes are left. Sophia has been rather absent recently ..."
        elif inputVal==4:
            return
        else:
 	        print"\ninvalid choice\n"

def garage():
        print "In the Garage you see Sophia's car is missing, the concrete is cool on your feet, where did she go?"
    while true:
        inputVal = input("Your choices are:\n1.Look through the window\n2.Return to Hallway")
        if inputVal==1:
            print "You look through the window, there are no cars in sight. It is a sunny and beautiful day ..."
            print "you wish you could go outside for a bit ..."
        elif inputVal==2:
            return
        else:
            print"\ninvalid choice\n"

def garage():
    print"You enter the Garage, the concrete is cool on your feet. You see that Sophia's car is missing, where did she go?"
while true:
    inputVal = input("Your choices are:\n1.Look through the window\n2.Return to Hallway\nSelect choice: ")
    if inputVal==1:
        print "You look through the window, there are no cars in sight. It is a sunny and beautiful day ..."
        print "you wish you could go outside for a bit ..."
    elif inputVal==2:
        return
    else:
        print"\nInvalid choice\n"

def window():
    print "You peek through the window, a bird flys by and you are distracted for a period of time ... "
#look through the window a second time and dont see bird D:

def livingRoom():
        print "In the living room and see a TV, Couch, and Coffee Table"
    while true:
        inputVal = input("Your choices are:\n1.TV\n2.Couch\n3.Coffee Table\n4.Return to Hallway")
        if inputVal==1:
            print "The TV is on, soothing music is playing."
        elif inputVal==2:
            print "You see a letter stuffed between the cushions... "
        elif inputVal==3:
            print "You look on the coffee table, there is a half finished cup of tea ... Sophia always finishes her tea"
        elif inputVal==4:
            return
        else:
            print"\ninvalid choice\n"

def bathroom():
        print "In the bathroom you see a Sink and Bathtub. Sophia didn't drain her last bath ... lazy"
    while true:
        inputVal = input("Your choices are:\n1.Sink\n2.Bathtub\n3.Return to Hallway")
        if inputVal==1:
	        print "You look at the sink, and see your reflection in the mirror. You look cute today :3"
        elif inputVal==2:
            print "You look at the bathtub and dip your foot in the water, it is cold and you are now upset"
            print "to the side of the tub you see a letter ... "
        elif inputVal==3:
            return
        else:
 	        print"\nInvalid choice\n"

def bedroom():
        print "In the bedroom you see a Bed, Dresser, and Nightstand. It's chilly in here."
    while true:
        inputVal = input("Your choices are:\n1.Bed\n2.Dresser\n3.Nightstand\n4.Return to Hallway")
        if inputVal==1:
	    print "You look at the bed, it is made nice and neat. You have an urge to get under the covers for a bit."
        print "so you do ..."
        elif inputVal==2:
            print "You look at the dressser, there is a letter ..."
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
	        livingroom()
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
        print "Letter #1"
    elif letter == 2:
        print "Letter #2"
    elif letter == 3:
        print "Letter #3"
    elif letter == 4:
        print "Letter #4"

print"-----------------------------------------"
print"            Wake up Simon"
print"-----------------------------------------"
print"    you wake up in the hallway. why did you fall asleep here? you stand up and stretch."
print"Where is Sophia? you need to find out where she went. better investigate.              "
energy=100
hallway()





