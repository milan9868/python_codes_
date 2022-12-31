import tkinter as tk
from tkinter import *
from tkinter import ttk

class Aero( Frame ):
    def __init__( self ):
        tk.Frame.__init__(self)
        self.pack()
        self.master.title("My_First_App")
        self.button1 = Button( self, text = "CLICK HERE", width = 25,
                               command = self.new_window )
        self.button1.grid( row = 0, column = 1, columnspan = 2, sticky = W+E+N+S )
    def new_window(self):
        self.newWindow = Aero_Uwu()
class Aero_Uwu(Frame):     
    def __init__(self):
        new =tk.Frame.__init__(self)
        new = Toplevel(self)
        new.title("Windows_HeHe")
        new.button = tk.Button(  text = "PRESS TO CLOSE", width = 25,
                                 command = self.close_window )
        new.button.pack()
    def close_window(self):
        self.destroy()
def main(): 
    Aero().mainloop()
if __name__ == '__main__':
    main()
  
    