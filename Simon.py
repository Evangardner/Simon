def kitchen():
    print "You enter the Kitchen and see a Fridge, Stove, and Table ... "

    while True: 
        inputVal = input("Your choices are:\n1.Fridge\n2.Stove\n3.Table\n4.Return to Hallway\nSelect choice: ")
        if inputVal==1:
	        print "\nYou look at the fridge, you stomach grumbles ... you are hungry"
        elif inputVal==2:
            print "\nYou look at the stove, there is a letter sitting on top ... who left this? Sophia?"
            letter(1) #TODO figure out how we want to do the letters: Have a date stamp? or Assign the letters dynamically?
        elif inputVal==3:
            print "\nYou look at the table, yesterdays dirty dishes are left. Sophia has been rather absent recently ..."
        elif inputVal==4:
            return
        else:
 	        print"\nInvalid choice\n"

def garage():
    print""

def window():
    print""

def livingRoom():
    print""

def bathroom():
    inputVal = input("\nSelect choice: ")
    if inputVal==1:
	    print""
    elif inputVal==2:
        print""
    elif inputVal==3:
        return
    else:
 	    print"\nInvalid choice\n"

def bedroom():
    inputVal = input("\nSelect choice: ")
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





