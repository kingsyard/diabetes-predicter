# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 13:02:56 2019

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 08:41:06 2019

@author: user
"""

#q=pd.read_csv("predict2.csv")
#p=q['Review']
#pp=(p)
import tkinter
from tkinter import Button
from tkinter import Entry
window = tkinter.Tk()
from tkinter.font import Font 
from tkinter import messagebox
# to rename the title of the window 
window.title("INTELLIGENT CLASSIFICATION SYSTEM FOR DIABETES")
window.geometry('400x400') 
# pack is used to show the object in the window

label0 = tkinter.Label(window, text = "Project Name :Intelligent classification for diabetes " ,font=("Arial Bold", 10))
label0.grid(column=0,row=1) 
label01 = tkinter.Label(window, text = "Branch: CSE" ,font=("Arial Bold",30))
label01.grid(column=0,row=2) 


label1 = tkinter.Label(window,text = "id",background="black", foreground="yellow")
label1.grid(column=0,row=12)
txt1 = Entry(window,width=30) 
txt1.grid(column=0,row=13)



#label12=tkinter.Label(window,text="'Mumbai Indians':1,'Chennai Super Kings':2,'Kolkata Knight Riders':3,'Royal Challengers Bangalore':4,'Kings XI Punjab':5,'Rajasthan Royals':6,'Delhi Daredevils':7,'Sunrisers Hyderabad':8,'Deccan Chargers':9,'Gujarat Lions':10,'Pune Warriors':11,'Rising Pune Supergiant':12,'Kochi Tuskers Kerala':13,'Rising Pune Supergiants':14") 
#label12.grid(column=4,row=5)
def clicked():
    
 
      id= txt1.get()
      #t={'MI':1,'csk':2}
      t1=int(id)
     
     
      a=data.loc[t1,:]
      

      
      label12 = tkinter.Label(window,text = "result displays here")
      label12.grid(column=0,row=31)
      label12.configure(text=a)
      
      
             
         
    #  label3.configure(text=pp[nn])    
 
bt=Button(window, text="Enter", command=clicked, height =2, width =5)

bt.grid (column=0, row=34)


window.mainloop()
#print(data)

  
        
        

