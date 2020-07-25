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
window.geometry('1600x800') 
# pack is used to show the object in the window

label0 = tkinter.Label(window, text = "Project Name :Intelligent classification for diabetes " ,font=("Arial Bold", 10))
label0.grid(column=0,row=1) 
label01 = tkinter.Label(window, text = "Branch: CSE" ,font=("Arial Bold",30))
label01.grid(column=0,row=2) 


label1 = tkinter.Label(window,text = "number of Pregnensies",background="black", foreground="yellow")
label1.grid(column=0,row=12)
txt1 = Entry(window,width=30) 
txt1.grid(column=0,row=13)

label3 = tkinter.Label(window,text = "Glucose Concentration",background="black", foreground="yellow")
label3.grid(column=0,row=14)
txt2 = Entry(window,width=30) 
txt2.grid(column=0,row=15)

label4 = tkinter.Label(window,text = "diastolic BP", background="black", foreground="yellow")
label4.grid(column=0,row=16)
txt3 = Entry(window,width=30) 
txt3.grid(column=0,row=17)

label5 = tkinter.Label(window,text = "insulin",background="black", foreground="yellow")
label5.grid(column=0,row=18)
txt4 = Entry(window,width=30) 
txt4.grid(column=0,row=19)

label6 = tkinter.Label(window,text = "bmi",background="black", foreground="yellow")
label6.grid(column=0,row=20)
txt5 = Entry(window,width=30)
txt5.grid(column=0,row=21)

label7 = tkinter.Label(window,text = "diabetic pedigree function",background="black", foreground="yellow")
label7.grid(column=0,row=22)
txt6 = Entry(window,width=30)
txt6.grid(column=0,row=23)

label8 = tkinter.Label(window,text = "age",background="black", foreground="yellow")
label8.grid(column=0,row=24)
txt7 = Entry(window,width=30)
txt7.grid(column=0,row=25)

label9 = tkinter.Label(window,text = "skin",background="black", foreground="yellow")
label9.grid(column=0,row=26)
txt8 = Entry(window,width=30)
txt8.grid(column=0,row=27)


label11 = tkinter.Label(window,text = "number of Pregnensies: 7 and more Diabetic ",foreground="red",font=("Courier",12))
label11.grid(column=1,row=12)
label11 = tkinter.Label(window,text = "Glucose Concentration : 105  and more Diabetic ",foreground="blue",font=("Courier",12))
label11.grid(column=1,row=14)
label11 = tkinter.Label(window,text = "diastolic BP :60  and more Diabetic ",foreground="black",font=("Courier",12))
label11.grid(column=1,row=16)
label11 = tkinter.Label(window,text = "Insulin: 126 and more Diabetic ",foreground="red",font=("Courier",12))
label11.grid(column=1,row=18)
label11 = tkinter.Label(window,text = "diabetic Pedigree Function :0.8 and less  Diabetic ",foreground="blue",font=("Courier",12))
label11.grid(column=1,row=20)
label11 = tkinter.Label(window,text = "age  : 30 and more Diabetic ",foreground="black",font=("Courier",12))
label11.grid(column=1,row=22)
label11 = tkinter.Label(window,text = "bmi  : inbetween 20-30",foreground="red",font=("Courier",12))
label11.grid(column=1,row=24)
label11 = tkinter.Label(window,text = "skin :10 and more Diabetic ",foreground="blue",font=("Courier",12))
label11.grid(column=1,row=26)

#label12=tkinter.Label(window,text="'Mumbai Indians':1,'Chennai Super Kings':2,'Kolkata Knight Riders':3,'Royal Challengers Bangalore':4,'Kings XI Punjab':5,'Rajasthan Royals':6,'Delhi Daredevils':7,'Sunrisers Hyderabad':8,'Deccan Chargers':9,'Gujarat Lions':10,'Pune Warriors':11,'Rising Pune Supergiant':12,'Kochi Tuskers Kerala':13,'Rising Pune Supergiants':14") 
#label12.grid(column=4,row=5)
def clicked():
    
 
      num_preg= txt1.get()
      #t={'MI':1,'csk':2}
      t1=int(num_preg)
      glucose_conc= txt2.get()
      t2=int(glucose_conc)
      diastolic_bp= txt3.get()
      vn=int(diastolic_bp)
      insulin= txt4.get()
      ct=float(insulin)
      bmi= txt5.get()
      ts=float(bmi)
      diab_pred= txt6.get()
      td=float(diab_pred)
      age= txt7.get()
      age1=int(age)
      skin= txt8.get()
      skin1=float(skin)
      X_test[0]=(t1,t2,vn,ct,ts,td,age1,skin1)
      predict= random_forest_model.predict(X_test)
      print(predict)
      w=predict[0]
      if w==0:
          
          messagebox.showinfo("RESULT","The patient is  Non Diabetic")
          messagebox.showinfo("warning","congradulation,you are perfect")
          
          
      else:
          
         
         
         
         total=((t1+t2+vn+ct+ts+td+age1+skin1)*(100))/698.6
         if total <= 57:
             
             messagebox.showinfo("RESULT","The patient is Diabetic in Stage 1")
             messagebox.showinfo("warning","visit to doctors ") 
         elif total >=90:
             
             messagebox.showinfo("RESULT","The patient is Diabetic in Stage 3")
             messagebox.showinfo("warning","its too late ,Time to Visit Best Doctors") 
         else:
             
             messagebox.showinfo("RESULT","The patient is Diabetic in Stage 2")
             messagebox.showinfo("warning","need to visit doctor very early") 
             
             
         
         
      
      
 
    #  label3.configure(text=pp[nn])    
 
bt=Button(window, text="Enter", command=clicked, height =2, width =5)

bt.grid (column=0, row=34)


window.mainloop()
#print(data)

  
        
        

