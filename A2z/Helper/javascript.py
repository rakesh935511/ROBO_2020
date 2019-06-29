# Import wx module 
import wx 
from time import sleep
# creaing application object 
app1 = wx.App() 

# creating a frame 
frame = wx.Frame(None, title ="wxpython app") 
frame.Maximize(maximize=True)
pa = wx.Panel(frame) 

# Button creation 
e = wx.Button(pa, -1, "Button1", pos = (500, 100))
e = wx.CheckBox(pa, -1, "CheckBox2", pos = (500, 120)) 
sleep(6)
# show it 
frame.Show() 

# start the event loop 
app1.Mainloop() 


        
        
    