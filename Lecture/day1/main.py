'''
Russell Schlup
DPW
1/6/13
'''

#print 'hello world'
'''
This is where I am learning about cool python syntax like avariable, expressions, conditionals, loops, and functions
'''
#single lined coment
firstName = 'Russell'
lastName = 'Schlup'
#print firstName+' '+lastName

yearBorn = 1993
age = 2014 - yearBorn
#print firstName+', you are '+age+' years old'

#format string function
message = '''{firstName}, you are {age} years old'''
messageFormatted = message.format(**locals())
#print messageFormatted

#Expressions
numPears = 6
#numPears++
#same as js

#conditionals
#if numPears == 6:
    #print 'I have 6 pears'

#if NumbPears < 6:
    #print 'I have less than six pears'
#else:
    #print 'I have 6 pears or more'

#else if
#if numPears == 2:
    #print 'duo pears!'
#elif numPears == 1:
    #print 'solo pears'
#else:
    #print 'you have something other than 1 0r 2 pears'

#arrays - lists
races = ['protoss','zerg','terran']
#print races[0]
#lastItem = races.pop()
#print races[1:3] #from ____ to _____

#dictionaries - associative arrays python - object
#data structures

#TV shows of students in DPW
shows = dict() #intantiating function
shows = dict(Ross='Bones', Russell='Scrubs', Jairo='Family Guy')
shows2 = {'Nate':'Board walk empire', 'Anthony':'House'}
shows3 = dict()
shows3['Mike']='Hostages'
shows3['Tyronne']='Sons of Anarchy'

#print shows3['Tyronne']

#funcitons - def
height = 60
width = 2

def calcArea(h,w):
    area = h * w
    return area
a = calcArea(height, width)
#print a

#code down here
def calcPerimeter():
    pass

#Loops
#for(var i=0;i<3;i++)
#for race in races:
    #print race
#for i in range(0,10):
    #print i

import random
print random.randrange(2,8)

#inputs
name = input('Type in your name.')
print name