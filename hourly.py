# pending items:
# 1 close form on submission
# 2 disable x button
# 3 full screen
# 4. task scheduler is not working after 12 AM night
# 5. DataTime difference   Return hours and minutes between 2 times: =TEXT(B2-A2, "h:mm")

# Set task scheculer for below
# 1 daily 
# 2 on workstation unlock
# 3 on logon
# 3 on startup


from tkinter import * 
import datetime as dt
import datetime

def save_info():
    taskdone_info     = taskdone.get()
    productivity_info = productiveVar.get()

    mydatetime = datetime.datetime.now()
    print(productivity_info , taskdone_info, mydatetime  )
    
    file = open("d:\hourly.txt","a")
    
    file.write( str(mydatetime) 	+ '\t'	+ 	','	+ 	'\t') 
    file.write( str(productivity_info)  + '\t'	+ 	','	+ 	'\t')
    file.write( taskdone_info           )
    file.write("\n")
    file.close()
    app.destroy()
    

app = Tk()

app.title("BREAK REMINDER !!")

# setting the windows size
app.geometry("1600x900")


heading = Label(text="BREAK REMINDER  -  Wash your FACE ",fg="black",bg="yellow",width="500",height="3",font="10")
heading.pack()

def sel():
   selection = "You selected the option " + str(productiveVar.get())
   label.config(text = selection)

#def Close():
#    app.destroy()
 

myOnScreenClock = Label( app, text=f"{datetime.datetime.now():%a, %b %d %Y}" , fg="white", bg="black", font=("helvetica", 40))
myOnScreenClock.pack()

firstname_text = Label(text="Enter Task Done in last One Hour :")
productive_text= Label(text="Productivity :")

taskdone = StringVar()
productiveVar = StringVar()
#value = StringVar() 


first_name_entry = Entry(textvariable=taskdone ,width="50" )
first_name_entry.place(x=15,y=170)

productive_option1_selected = Radiobutton(app, text="NON-Productive", variable=productiveVar , value="NON-Productive", command=sel)
productive_option1_selected.pack( anchor = W )
# UNSELECT BOTH radio buttons
productiveVar.set(0)

productive_option2_selected = Radiobutton(app, text=    "Productive", variable=productiveVar , value="Productive", command=sel)
productive_option2_selected.pack( anchor = W )
# UNSELECTs BOTH radio buttons
productiveVar.set(0)

first_name_entry.place(x=15,y=170)
productive_option1_selected.place(x=15,y=220)
productive_option2_selected.place(x=200,y=220)

firstname_text.place(x=15,y=150)
productive_text.place(x=15,y=200)

myOnScreenClock.place(x=15, y=80)






button = Button(app,text="Submit Data",command=save_info,width="30",height="5",bg="grey")
button.place(x=15,y=350)

label = Label(app)
label.pack()

 

 
mainloop()



