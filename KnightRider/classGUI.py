'''
Created on Feb 29, 2020

@author: marbe
'''
import tkinter as tk
from tkinter import Button

class classGUI(object):
    '''
    classdocs
    '''
    root = []
    canvas = []
    containerLED = []
    ledObj = []
    
    # init
    def __init__(self, ledObj):
        self.ledObj = ledObj
    
    # callback red button
    def callbackRed(self):
        # change color to red
        for n in range(len(self.ledObj)):
            self.ledObj[n].color = 0
            
    # callback green button
    def callbackGreen(self):
        # change color to red
        for n in range(len(self.ledObj)):
            self.ledObj[n].color = 1
    
    # callback green button
    def callbackBlue(self):
        # change color to red
        for n in range(len(self.ledObj)):
            self.ledObj[n].color = 2
            
    # create window method
    def createWindow(self, numLED):
        # create root
        self.root = tk.Tk()
        
        # name root
        self.root.title("Knight Rider Simulator")
        
        # size of canvas
        self.canvas = tk.Canvas(self.root, width=(numLED*60)+10, height=140)
        self.canvas.pack()
        
        # create container for LED
        self.containerLED = [] 
        
        # place LED arrcoding number of numLED
        for n in range(numLED):
            self.containerLED.append(self.canvas.create_oval((n*50)+(n*10)+10,25,(n*50)+60+(n*10),75, fill='white')) 
        
        # place red button
        b = Button(self.root, text="Red", width = 8, height = 1, command=self.callbackRed)
        b.pack()
        b.place(x = 10, y = 100)
        
        # place green button
        b = Button(self.root, text="Green", width = 8, height = 1, command=self.callbackGreen)
        b.pack()
        b.place(x = 100, y = 100)
        
        # place blue button
        b = Button(self.root, text="Blue", width = 8, height = 1, command=self.callbackBlue)
        b.pack()
        b.place(x = 190, y = 100)
        
    # change color method
    def turnOnLED(self, posLED, ledObj):
        if ledObj.color == 0:
            self.canvas.itemconfig(self.containerLED[posLED], fill='red')
        elif ledObj.color == 1:
            self.canvas.itemconfig(self.containerLED[posLED], fill='green')
        else:
            self.canvas.itemconfig(self.containerLED[posLED], fill='blue') 
            
    def turnOffLED(self, posLED):
        self.canvas.itemconfig(self.containerLED[posLED], fill='white')