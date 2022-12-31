import pyautogui
import tkinter as tk

root = tk.Tk()
root.title('Screenshotographer')

canvas1 = tk.Canvas(root, width = 200, height = 200)
canvas1.pack()

def myScreenshot():
    
    sc = pyautogui.screenshot()
    sc.save(r"F:\ScreenShots\screenshot.png")
    
myButton = tk.Button(text = 'Capture', command = myScreenshot, bg = 'white', fg = 'black', font = '20')
canvas1.create_window(200, 200, window = myButton)



root.mainloop()
