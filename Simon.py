def kitchen():
    while True: 
        print "You enter the Kitchen and see a Fridge, Stove, and Table ... "
        inputVal = input("Your choices are:\n1.Fridge\n2.Stove\n3.Table\n4.Return to Hallway")
        if inputVal==1:
	        print "You look at the fridge, you stomach grumbles ... you are hungry"
        elif inputVal==2:
            print "You look at the stove, there is a letter sitting on top ..."
#add in stuff for reading letter twice etc ... ADD COUNTER, for first letter, write some specific statements etc
        elif inputVal==3:
            print "You look at the table, yesterdays dirty dishes are left. Sophia has been rather absent recently ..."
        elif inputVal==4:
            return
        else:
 	        print"invalid choice"

def garage():
    print"You enter the Garage, the concrete is cool on your feet. You see that Sophia's car is missing, where did she go?"
    
    inputVal = input("Your choices are:\n1.Look through the window\n2.Return to Hallway")
    if inputVal==1:
        print "You look through the window, there are no cars in sight. It is a sunny and beautiful day ..."
        print "you wish you could go outside for a bit ..."
    elif inputVal==2:
        return
    else:
        print"invalid choice"

def window():
    print"You peek through the window, a bird flys by and you are distracted for a period of time ... "
#look through the window a second time and dont see bird D:

def livingRoom():
    print"You enter the living room and see a TV, Couch, and Coffee Table"
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
        print"invalid choice"

def bathroom():
    inputVal = input("Your choices are:\n\nSelect choice: ")
    if inputVal==1:
	    print""
    elif inputVal==2:
        print""
    elif inputVal==3:
        return
    else:
 	    print"\nInvalid choice\n"

def bedroom():
    inputVal = input("Your choices are:\n\nSelect choice: ")
    if inputVal==1:
	print""
    elif inputVal==2:
        print""
    elif inputVal==3:
        print""
    elif inputVal==4:
        print""
    elif inputVal==5:
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





