# import wx module 
import wx 
from time import sleep

# creaing application object 
app1 = wx.App() 

# creating a frame 
frame = wx.Frame(None, title ="RAKESH") 
frame.Maximize(maximize=True)
pa = wx.Panel(frame)
 

# Adding a text to the frame object 
text1 = wx.StaticText(pa, label ="GEEKS FOR GEEKS", pos =(100, 50)) 
sleep(10)
# show it 
frame.Show() 

# start the event loop 
app1.Mainloop() 
