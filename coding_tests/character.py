'''
Created on Jan 11, 2016

@author: eduardo.torres
'''
class character():
    
    def __init__(self):
        self.type       = None
        self.attack     =   4
        self.defense    =   4
        self.speed      =   4
        self.inventory  = {1,2,3,4,5,6}
    
    def menu(self):
        print "Please type the option you'd like to choose"
        print "STATUS"
        print "INVENTORY"
        print "EXIT"
        
        option = raw_input()
        
        if option == "STATUS":
            print "Attack: ",
            print self.attack
            print "Defense: " ,
            print self.defense
            print "Speed: " ,
            print self.speed
        elif option == "INVENTORY":
            for id in self.inventory:
                print id
        
        elif option == "EXIT":
            print "EXITING MENU"
            
        else:
            print "Nah man, you got it wrong"