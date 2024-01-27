from tkinter import *
from tkinter import ttk
#calling function
def sum():
    global elseentry, bmientry, stmtentry
    nameresult=nameentry.get()
    print("name :",nameresult)
    drops = drop.get()
    print("drops:", drops)
    feetresult=feetentry.get()if feetentry else None
    print("feet_result :",feetresult)
    inchresult=inchentry.get()if inchentry else None
    print("inch_result :",inchresult)
    metersresult=meterentry.get()if meterentry else None
    print("meters_result :",metersresult)
    cmresult=cmentry.get()if cmentry else None
    print("cm_result :",cmresult)
    weightresult=weightentry.get()
    print("weight_result :",weightresult)
    global elseentry,bmientry,stmtentry
    import Backend
    bmiresult,stmtresult,elsex=Backend.logic(drops,feetresult,inchresult,metersresult,cmresult,weightresult,nameresult)
    print(bmiresult)
    print(stmtresult)
    print(elsex)
    if elsex=="":

        if bmientry and stmtentry:
            bmientry.destroy()
            stmtentry.destroy()
        result = StringVar()
        bmientry = Entry(root, textvariable=result,width=65,**entry_style)
        bmientry.place(x=300, y=550)
        result.set(bmiresult)
        output = StringVar()
        stmtentry = Entry(root, textvariable=output,width=65,**entry_style)
        stmtentry.place(x=300, y=600)
        output.set(stmtresult)
    else:
        if elseentry:
            elseentry.destroy()
        
        if bmientry:
            bmientry.destroy()
        if stmtentry:
            stmtentry.destroy()
        resultelsex = StringVar()
        elseentry = Entry(root, textvariable=resultelsex,width=65,**entry_style)
        elseentry.place(x=300, y=600)
        resultelsex.set(elsex)

feetentry = None
inchentry = None
meterentry=None
cmentry=None
inches=None
feet=None
meters=None
cm=None
drops = None
elseentry = None
bmientry = None
stmtentry = None
def dropdown_call(event):
    global feetentry, inchentry
    global meterentry,cmentry
    global inches,feet
    global meters,cm
    global drops
    global bmiresult,stmtresult,elsex
    drops = drop.get()
    if feetentry:
        feetentry.destroy()
        feet.destroy()
        feetentry = None
    if inchentry:
        inchentry.destroy()
        inches.destroy()
        inchentry = None
    if meterentry:
        meterentry.destroy()
        meters.destroy()
        meterentry = None
    if cmentry:
        cmentry.destroy()
        cm.destroy()
        cmentry = None
    
    if drops == "feet and inches":
        feet = Label(root, text="FEET",font=("Arial", 20), fg="blue", bg="lightgrey", padx=10, pady=5)
        feet.place(x=350, y=300)
        inches = Label(root, text="INCHES",font=("Arial", 20), fg="blue", bg="lightgrey", padx=10, pady=5)
        inches.place(x=850, y=300)
        feetval = StringVar()
        inchval = StringVar()
        feetentry = Entry(root, textvariable=feetval,**entry_style)
        feetentry.place(x=500,y=300)
        inchentry = Entry(root, textvariable=inchval,**entry_style)
        inchentry.place(x=1000, y=300)
    elif drops == "meters":
        meters = Label(root, text="METERS",font=("Arial", 20), fg="blue", bg="lightgrey", padx=10, pady=5)
        meters.place(x=600, y=300)
        meterval = StringVar()
        meterentry = Entry(root, textvariable=meterval,**entry_style)
        meterentry.place(x=800, y=300)
    else:
        cm = Label(root, text="CENTIMETERS",font=("Arial", 20), fg="blue", bg="lightgrey", padx=10, pady=5)
        cm.place(x=600, y=300)
        cmval = StringVar()
        cmentry = Entry(root, textvariable=cmval,**entry_style)
        cmentry.place(x=900, y=300)

root = Tk()
root.title("Dropdown Example")
root.geometry("1300x800")        
root['bg']='#ffbf00'

#drop down
drop= StringVar()
dropdown = ttk.Combobox(root, textvariable=drop)
dropdown['values'] = ("feet and inches", "meters", "centimeters")
dropdown.place(x=600,y=200)
dropdown.bind("<<ComboboxSelected>>",dropdown_call)
dropdown.config(height=1000)
dropdown.config(font=('Arial', 10))
dropdown.config(width=50)
Label(root,text="BMI CALCULATOR",font="ar 15 bold").grid(row=0,column=0,sticky='nsew')
root.grid_columnconfigure(0, weight=1)
name = Label(root, text="NAME", font=("Arial", 20), fg="blue", bg="lightgrey", padx=50, pady=5)
name.place(x=300,y=100)
height=Label(root,text="HEIGHT IN",font=("Arial", 20), fg="blue", bg="lightgrey", padx=50, pady=5)
height.place(x=300,y=200)
weight=Label(root,text="WEIGHT",font=("Arial", 20), fg="blue", bg="lightgrey", padx=50, pady=5)
weight.place(x=300,y=400)
entry_style = {'font': ('Arial', 20), 'bd': 2, 'relief': SOLID, 'highlightthickness': 1}
#declaring type
nameval=StringVar()                     
weightval=StringVar()
nameentry=Entry(root,textvariable=nameval,**entry_style)
nameentry.place(x=600,y=100)
weightentry=Entry(root,textvariable=weightval,**entry_style)
weightentry.place(x=600,y=400)
#Submit Button
button=Button(root,text="SUBMIT",command=sum, bg="blue", fg="white",width=20, height=2)
button.place(x=600,y=500)
root.mainloop()

            
                
            
                
                    
            



