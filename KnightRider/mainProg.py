'''
Created on Feb 29, 2020

@author: marbe
'''
#import classes
from classLED import classLED
from classGUI import classGUI

# parameters
numLED = 10
direction = 0
mover = 0

# create LED objects
myLEDs = []
for n in range(numLED):
    myLEDs.append(classLED)
    myLEDs[n].color = 1;

# run methode
def task():
    # assign local variables
    global numLED
    global direction
    global mover
    
    # move left
    if direction == 0:
        guiObj.turnOnLED(mover, myLEDs[mover])
        
        # turn off previous LED when is not < 0
        if mover > 0:
            guiObj.turnOffLED(mover-1)    
        
        # move further  
        mover +=  1
        
        # change direction
        if mover >= numLED:
            direction = 1
            mover -= 2
            
    # move left
    elif direction == 1:
        guiObj.turnOnLED(mover, myLEDs[mover])
        
        # turn off previous LED when is not > numLED
        if mover < numLED-1:
            guiObj.turnOffLED(mover+1)   
        
        # move further
        mover -= 1
        
        # change direction
        if mover < 0:
            direction = 0
            mover += 2
        
    # start next iteration    
    guiObj.root.after(40,task)
        
# create GUI object
guiObj = classGUI(myLEDs)

# create Window
classGUI.createWindow(guiObj, numLED)

# run tkinter
guiObj.root.after(1000, task)
guiObj.canvas.mainloop()
