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
	    print("invalid choice")
	
def energyBar():
    print "Energy Level "+energy+"%"

def hallway():
    while True:
        print "you are in the hallway"
        print "your choices are:\n1.Bedroom\n2.Bathroom\n3.Kitchen\n4.Garage\n5.Window\n6.Living Room"
	inputVal = input("\nEnter your choice:")

print"-----------------------------------------"
print"            Wake up Simon"
print"-----------------------------------------"
print"    you wake up in the hallway. why did you fall asleep here? you stand up and stretch."
print"Where is Sophia? you need to find out where she went. better investigate.              "
hallway()





