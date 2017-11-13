#Python Programming Fundamentals by Kent Lee
#https://www.youtube.com/watch?v=jmjTAXbH-SA&index=1&list=PL1DE477438120C9EF
#http://knuth.luther.edu/~leekent/IntroToComputing/

#Convert raw_input (python 2.*) to input (pytohn 3.*)
def input(msg):
    return raw_input(msg)
#if hasattr(__builtins__, 'raw_input'):
    #input=raw_input
        
#width = input('Please enter the width of the container in cm: ')
#height = input('Please enter the height of the container in cm: ')
#depth = input('Please enter the depth of the container in cm: ')
#volume = width * height * depth
#print 'The volume is', volume
#ounces = volume/29.573529688
#gallons = int(ounces/128)
#ounces = ounces-gallons*128
#print 'The number of gallons of water in this container could be', gallons, 'and','%1.2f' %ounces,'ounces'

#if-else statemnent: find the geatest among three numbers
#x = input('Please enter an integer: ')
#y = input('Please enter an integer: ')
#z = input('Please enter an integer: ')
#if x > y:
    #if x > z:
        #print  x, 'is the greatest'
    #else:
        #print x, 'is the greatest'
#else:
    #if y>z:
        #print y, 'is the greatest'
    #else:
        #print z, 'is the greatest'        
#print 'Done'

##2-1 Guess & Check Pattern: Find the greatest among three numbers
#x = input('Please enter an integer: ')
#y = input('Please enter an integer: ')
#z = input('Please enter an integer: ')
##Make a Guess
#maxVal = x
##Check my Guess
#if maxVal<y:
    ##Fix my Guess
    #maxVal = y
#if maxVal<z:
    ##Fix my Guess
    #maxVal = z
#print maxVal, 'is the greatest'
#print 'Done'

##2-2 Boolean
#name = input ('What is your name? ')
#mustRegister = True
#gender = input ('Please enter your gender (M/F)? ')
#if gender == "F":
    #mustRegister = False
#visa = input ('Are you here on a student or visitor visa (Y/N)? ')
#if visa == 'Y':
    #mustRegister = False
#hospitalized = input ('Are you hospitalized (Y/N)? ')
#if hospitalized == 'Y':
    #mustRegister = False
##More conditions
#if mustRegister:
    #print 'You must register for the selective service.'
#else:
    #print 'You do not need to register for the selective service at this time'

##2-3 Comparing Floats
#import random
#x=random.random()
#xVal = int(x * 10000)/100
#y=random.random()
#yVal = int(y * 10000)/100
#answer = float(input('Waht is the value ' + str(xVal)+'-'+str(yVal)+' equal to? '))
#realAnswer = xVal - yVal
#if abs((answer - realAnswer)/realAnswer) < 0.001:
    #print 'You did it!'
#else:
    #print 'No, the answer was', realAnswer
    
##3-1 Iterating over a sequence: For-loop
#name = input ('Please enter your name:')
#for c in name:
    ##c = next character in name
    #print c
#print'next example'
#for i in range(0,len(name),2):
    #print name[i]
#print'example 3'
#for i in range(len(name)-1,-1,-1):
    #print name[i]

##3-2 Nested For-loops
#print '      ',
#for i in range(16):
    #print '%5d|'%i,
#print '\n'
#print '_______'*17
#for i in range(16):
    #print '%5d|'%i,
    #for j in range(16):
        #print '%5d|'%(i*j),
    #print'\n'

##3-3 Guess & Check for Lists
#primes = [2,3,5,7]
#x = int(input("Please enter an integer between 2 and 49: "))
##Make a guess
#isPrime = True
##Go through a list to determine if our guess was wrong
#for p in primes:
    #if x%p == 0 and not x in primes:
        #isPrime = False
#if isPrime:
    #print x,' is prime.'
#else:
    #print x, 'is not prime.'
    
##3-4 Accumulator Pattern for Lists
#s = input("Please enter a sentence: ")
#lst = s.split()
##INitialize our accumulators
#count = 0
#wordlengths = 0
##A for loop to go thru our list
#for word in lst:
    ##increment by accumulators
    #count = count + 1
    #wordlengths = wordlengths + len(word)
#avgWordLength = wordlengths / count
#print 'The sentence you enter had', count, 'words in it and the average word length was %1.2f.' %avgWordLength
        
##4-1 Creating & Using Objects
#import turtle
##CAll the Turtle Constructor to create a turtle object
#t = turtle.Turtle()
##getscreen is an accessor method on turtle objects
#screen = t.getscreen()
#for i in range(5):
    ##mutator methods change the object
    #t.forward(200)
    #t.left(144)
#screen.exitonclick()

##4-2 Plotting Data using Python and Turtle Graphics
#import turtle
#import datetime
#import math
#file = open('djia-100.txt','r')
#maxDJIA = 0
#startDate = datetime.datetime(1900,1,1)
#maxDate = startDate
#endDate = datetime.datetime(1999,12,31)
#minDate = endDate
#for line in file:
        #lst = line.split(',')
        #dateStr = lst[0]
        #djia = math.log10(float(lst[1]))
        ##if cnt == 3: print dateStr, djia, maxDJIA, line
        #year = int(dateStr[0:2])+1900
        #month = int(dateStr[2:4])
        #day = int(dateStr[4:6])
        #date = datetime.datetime(year,month,day)
        ##if cnt == 3: print month,day,year, date
        #if djia > maxDJIA:
            #maxDJIA = djia
        #if date > maxDate:
            #maxDate = date        
        #if date < minDate:
            #minDate = date        
#dateDiff = maxDate - minDate
#totalDays = dateDiff.days
#print 'maxDate=',maxDate, 'minDate=',minDate, 'dateDiff=',dateDiff
#print 'maxDJIA=',maxDJIA
#t = turtle.Turtle()
#screen = t.getscreen()
#screen.setworldcoordinates(0,0,totalDays,maxDJIA)
#t.goto(0,0)
#file.close()
#file = open('djia-100.txt','r')
#screen.tracer(100)
#t.color('#7D7EC0')
#t.fillcolor('#7D7EC0')
#t.begin_fill()
#for line in file:
        #lst = line.split(',')
        #dateStr = lst[0]
        #djia = math.log10(float(lst[1]))
        #year = int(dateStr[0:2])+1900
        #month = int(dateStr[2:4])
        #day = int(dateStr[4:6])
        #date = datetime.datetime(year,month,day)
        #dateDiff = date - minDate
        #t.goto(dateDiff.days, djia)
#t.goto(totalDays,0)
#t.end_fill()
#screen.update()
#screen.exitonclick()

##4-3 Dictionaries: mapping keys to values 
#dictionary={}   #key
#dictionary['Kent'] = 0
#dictionary['Sophus'] = 1
#dictionary['Lee'] = 2
#for key in dictionary:
    #print 'key=',key,'dictionary==',dictionary[key]
#pets={} #value
#pets['Kent']='Mesa'
#pets['Sophus']='Smudge'
#pets['Lee']='Lassie'
#for owner in dictionary:
    #petName=pets[owner]
    #print 'owner=',owner, 'petName=',petName
#pets['Alex']='Mesa'
#pets['Joshua']='Mesa'
#print 'pets=',pets

##4-4 Parsing XML Files
#from xml.dom import minidom
#xmldoc = minidom.parse('kml.kml')
#print 'xmldoc=',xmldoc
#kml = xmldoc.getElementsByTagName('kml')[0]
##print 'xml=',xml
#document = kml.getElementsByTagName('Document')[0]
#print 'document=',document
#placemarks = document.getElementsByTagName('Placemark')
#for placemark in placemarks:
    #desc = placemark.getElementsByTagName('description')[0].firstChild.data
    #lst = desc.split(':')
    #population = int(lst[1].split('<')[0])
    #coords = placemark.getElementsByTagName('coordinates')[0].firstChild.data
    #lst2 = coords.split(',')
    #longitude = float(lst2[0])
    #latitude = float(lst2[1])
    #cityName = placemark.getElementsByTagName('name')[0].firstChild.data
    #print cityName+':', longitude, latitude, population
    
##4-5 Attributes in XML Files
#from xml.dom import minidom
#from datetime import * #import anything in datatime module
#xmldoc = minidom.parse('biking3-15-2012.tcx')
#tcd = xmldoc.getElementsByTagName('TrainingCenterDatabase')[0]
#activitiesElement = tcd.getElementsByTagName('Activities')[0]
#activites = activitiesElement.getElementsByTagName('Activity')
#for activity in activites:
    #sport = activity.attributes['Sport']
    #sportName = sport.value       
    #idElement = activity.getElementsByTagName('Id')[0].firstChild.data   
    #year = int(idElement[0:4])
    #month = int(idElement[5:7])
    #day = int(idElement[8:10])
    #date = datetime(year,month,day)    
    #print sportName, date

##5-1 Defining & Calling Functions
#def f(x):
    #return x*x*x
#import turtle
#t = turtle.Turtle()
#screen = t.getscreen()
#screen.setworldcoordinates(-10,-10,10,10)
##Draw the axis
#t.goto(-10,0), t.goto(10,0)
#t.penup(), t.goto(0,-10), t.pendown(), t.goto(0,10)
##Draw the function graph
#t.penup()
#t.goto(-20,-20)
#t.pendown()
#for k in range(-30,30,1):
    #myx = k/10.0
    #myy = f(myx)
    #t.goto(myx,myy)
#screen.exitonclick()

##5-2 Functions & Scope
#import math
#def Polar_to_X(theta,r):
    #x = r*math.cos(theta)
    #return x
#def Polar_to_Y(theta,r):
    #y = r*math.sin(theta)
    #return y
#x = Polar_to_X(math.pi,1)
#y = Polar_to_Y(math.pi,1)
#print 'x=',x,'y=',y

#5-3 Run-time Stack
#F7 to activate debugging mode line by line
#check Stak Data\variables

##5-4 Bottom-up Design (draing a flower)
#import math
#def toRadians(deg):
    #return math.radians(deg) #deg/180.0 * math.pi
#def Polar_to_X(theta,r):
    #x = r*math.cos(theta)
    #return x
#def Polar_to_Y(theta,r):
    #y = r*math.sin(theta)
    #return y
#import turtle
#def drawPetal(t,x,y,angle):
    #t.penup()
    #t.goto(x,y)
    #t.pendown()    
    #for k in range(101):
        #theta = k/100.0 * math.pi/3 #pi/3 making 6 petals in 2 pi (circle)
        #r = 80 * math.sin(3*theta)  #radius increases (0~pi/2) and decreases (pi/2~pi) w max_r=80
        #xv = Polar_to_X(theta+angle,r)
        #yv = Polar_to_Y(theta+angle,r)
        #t.goto(x+xv,y+yv)
#def drawFlower(t,x,y):
    #for k in range(6):
        #angle = k*360.0/6
        #drawPetal(t,x,y,toRadians(angle))
#t = turtle.Turtle()
#screen = t.getscreen()
#screen.setworldcoordinates(-100,-100,100,100)
#drawFlower(t,0,0)
#screen.exitonclick()

##5-5 Main Function
#import math
#import turtle
#def toRadians(deg):
    #return math.radians(deg) #deg/180.0 * math.pi
#def Polar_to_X(theta,r):
    #x = r*math.cos(theta)
    #return x
#def Polar_to_Y(theta,r):
    #y = r*math.sin(theta)
    #return y
#def drawPetal(turtle,x,y,scale,color,angle):
    #turtle.penup()
    #turtle.goto(x,y)
    #turtle.pendown()    
    #turtle.color(color)
    #turtle.begin_fill()
    #for k in range(101):
        #theta = k/100.0 * math.pi/3 #pi/3 making 6 petals in 2 pi (circle)
        #r = scale*80 * math.sin(3*theta)  #radius increases (0~pi/2) and decreases (pi/2~pi) w max_r=80
        #xv = Polar_to_X(theta+angle,r)
        #yv = Polar_to_Y(theta+angle,r)
        #turtle.goto(x+xv,y+yv)
    #turtle.end_fill()
#def drawFlower(turtle,x,y,scale,color):
    #screen = turtle.getscreen()
    #screen.tracer(2) #speed up the drawing
    #for k in range(6):
        #angle = k*360.0/6
        #drawPetal(turtle,x,y,scale,color,toRadians(angle))
    #for k in range(10):
        #angle = k*360.0/10
        #drawPetal(turtle,x,y,scale*0.1,'black',toRadians(angle))
#def main(): #protecting variables inside main()
    #t = turtle.Turtle()
    #screen = t.getscreen()
    #screen.setworldcoordinates(-100,-100,100,100)
    #drawFlower(t,0,0,0.5,'lightblue')
    #screen.exitonclick()
#if __name__  == '__main__':
    #main()
    
##Calling flower.py as a module
#import flower
#import turtle
#def main():
    #t = turtle.Turtle()
    #screen = t.getscreen()
##    screen.setworldcoordinates(-100,-100,100,100)
    #flower.drawFlower(t,0,0,2,'blue')
    #flower.drawFlower(t,50,50,0.5,'pink')
    #screen.exitonclick()
#if __name__ == '__main__':
    #main()

##6-1 Tkinter
#import Tkinter as tk #for Python 2.*, cf)tkinter for Python 3.*
#import turtle
#import sys
#def main():
    #root = tk.Tk()  #create a window
    #root.title("Draw!")
    ##create a widget (element of GUI) of canvas 
    #cv = tk.Canvas(root,width=600,height=600)
    #cv.pack(side=tk.LEFT)   #control the layout thru packing
    ##assign cv as turtle's canvas
    #t = turtle.RawTurtle(cv)
    #screen = t.getscreen()
    #screen.setworldcoordinates(0,0,600,600)
    ##create a widget of frame
    #frame = tk.Frame(root,)
    #frame.pack(side=tk.RIGHT,fill=tk.BOTH)
    #screen.tracer(0)
    #def quitHandler():
        #print('Goodbye')
        #sys.exit(0)
    ##create a button
    #quitButton = tk.Button(frame,text='Quit',command=quitHandler)    
    #quitButton.pack()   #create a pack
    ##create an entry object
    #textLab = tk.Label(frame,text='Text to Write')
    #textLab.pack()
    #textVar = tk.StringVar()
    #textVar.set('Hello World')
    #textEntry = tk.Entry(frame,textvariable=textVar)
    #textEntry.pack()
    #def writeHandler():
        #t.write(textVar.get())
    #writeButton = tk.Button(frame,text='Write',command=writeHandler)    
    #writeButton.pack()   #create a pack      
    #def clickHandler(x,y):
        #t.goto(x,y)
        #screen.update() #prevent turtle's own update causing stack overflow
    #screen.onclick(clickHandler) 
    #def dragHandler(x,y):   #need to drag the turtle, not the mouse
        #t.goto(x, y)
        #screen.update()
    #t.ondrag(dragHandler)
    #tk.mainloop()   #listen to window event
#if __name__ == '__main__':
    #main()

##7-1 OOP
##Define a class of cat
#class Cat:
    #def __init__(self,name,age,weight):
        #self.name = name
        #self.age = age
        #self.weight = weight
        #self.stomach = 0
    #def feed(self,amount):
        #self.stomach = self.stomach + amount
    #def nextDay(self):
        ##It takes 1/4 lb of cat feed/day to keep a cat alive
        #self.weight = self.stomach + self.weight - 0.25
        #self.stomach = 0
    #def speak(self):
        #if self.stomach > 0: return 'purrrrr'
        #else:                return 'meow!!!'
    #def getName(self):
        #return self.name
    #def getWeight(self):
        #return self.weight
##create two objects of cat1 and cat2
#def main():
    #cat1 = Cat('Curious',10,7.2)
    #cat2 = Cat('Mother',15,14.3)
    #print cat1.getName(),'says',cat1.speak()
    #print cat2.getName(),'says',cat2.speak()
    #cat1.feed(2)
    #cat2.feed(1)
    #print cat1.getName(),'says',cat1.speak()
    #print cat2.getName(),'says',cat2.speak()
    #cat1.nextDay()
    #cat2.nextDay()
    #print cat1.getName(),'weighs',cat1.getWeight()
    #print cat2.getName(),'weighs',cat2.getWeight()
#if __name__ == '__main__':
    #main()

#7-2 Inheritance
from turtle import *
class FlipTurtle(Turtle):   #inheritance
    def __inti__(self):
        super(FlipTurtle,self).__init__()
    def left(self,val):
        super(FlipTurtle,self).right(val)
    def right(self,val):
        super(FlipTurtle,self).left(val)
    def forward(self,val):
        super(FlipTurtle,self).backward(val)
    def backward(self,val):
        super(FlipTurtle,self).forward(val)
def main():
    #test inheritance
    #t = Turtle()
    t = FlipTurtle()
    screen = t.getscreen()
    #screen.tracer(0)
    t.begin_fill()
    t.fillcolor('red')
    t.forward(50)               #t.goto(50,0)
    t.left(90), t.forward(30)   #t.goto(50,30) 
    t.left(90), t.forward(20)   #t.goto(30,30)
    t.right(45), t.forward(30)  #t.goto(20,50)
    t.left(45), t.forward(20)   #t.goto(0,50)
    t.left(90), t.forward(20)   #t.goto(0,30)
    t.right(90), t.forward(50)  #t.goto(-50,30)
    t.left(90), t.forward(31)  #t.goto(-50,0)
    t.left(90), t.forward(62)   #t.goto(0,0)
    t.end_fill()
    t.penup()    
    t.forward(20), t.right(90), t.forward(10) #t.goto(30,-20)
    t.begin_fill()
    t.fillcolor('black')
    t.circle(10)
    t.end_fill()
    t.penup()
    t.backward(10)
    t.right(90)
    t.forward(60) #t.goto(-30,-20)
    t.begin_fill()
    t.fillcolor('black')
    t.circle(10)
    t.end_fill()
    t.ht()  #hide turtle
    screen.exitonclick()
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    