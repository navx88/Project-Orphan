'''
Created on Jan 11, 2016

@author: eduardo.torres
'''
from character import *
import time
import random
from distutils.tests.test_register import RawInputs


print "Welcome to the game"
print "Please choose your class (hero, not-hero, derp)"
    
hero = character()
    
while hero.type == None:
        
    Class   =   raw_input("Pick one?")
        
    if Class == 'hero':
        hero.type   =   "hero"
        print "gg buddy"
        
    elif Class == 'not-hero':
        hero.type   =   "not-hero"
            
    elif Class == 'derp':
        hero.type   =   "derp"
    else:
        print "You done goofed. Try again"
            
hero.menu()