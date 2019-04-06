def kitchen():
    print""
def garage():
    print""
def window():
    print""
def livingRoom():
    print""
def bathroom():
    inputVal = input("Select choice")
    if inputVal==1:
	print""
    elif inputVal==2:
        print""
    elif inputval==3:
        return
    else:
 	print"invalid choice"

def bedroom():
    inputVal = input("Select choice")
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
	print"invalid choice"
	
def energyBar():
    global energy
    print "Energy Level ",energy,"%"

def hallway():
    
    while True:
        print "you are in the hallway"
        energyBar()
        global energy
        if energy>0:
	        energy = energy-10
        if energy == 0:
            print "your'e dead as fuck bro"
            return
        print "your choices are:\n1.Bedroom\n2.Bathroom\n3.Kitchen\n4.Garage\n5.Window\n6.Living Room\n7.Nap"
        inputVal = input("\nEnter your choice:")
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
        else:
	        print "invalid entry"

def nap():
   global energy
   if energy == 0:
       print "Napping..."
       energy = 100

print"-----------------------------------------"
print"            Wake up Simon"
print"-----------------------------------------"
print"    you wake up in the hallway. why did you fall asleep here? you stand up and stretch."
print"Where is Sophia? you need to find out where she went. better investigate.              "
energy=100
hallway()





