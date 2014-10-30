#########################################
#
#         85pt - Add a cancel button
#
#########################################


# Add a cancel button with a red background
# When the cancel button is pressed, change the color from red to blue
# and then back to red when pressed again
# Read the comment above line 24
from Tkinter import *

class MyApp:
	def __init__(self, parent):
		self.myParent = parent  ### (7) remember my parent, the root
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.button1 = Button(self.myContainer1)
		self.button1.configure(text="OK", background= "green")
	        self.button3 = Button(self.myContainer1)	
		# Do not change <Button-1> when you create Button 2 :)
		self.button1.bind("<Button-1>", self.button1Click) ### (1)
		
		self.buttoncan = Button(self.myContainer1)
		self.buttoncan.configure(text="cancel", background ="red")
		self.buttoncan.grid(row = 1, column=0)
		self.buttoncan.bind("<Button-1>", self.buttoncanClick)
		
		
	def button1Click(self, event):    ### (3)
		if self.button1["background"] == "green": ### (4)
			self.button1["background"] = "yellow"
		else:
			self.button1["background"] = "green"


        def buttoncanClick(self,event):
            if self.buttoncan["background"] == "blue":
                     self.buttoncan["background"] = "red"
            else:
                     self.buttoncan["background"] = "blue"         
		
		

		
	
		
root = Tk()
myapp = MyApp(root)
root.mainloop()