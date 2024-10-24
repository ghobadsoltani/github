from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Ghobad Soltani")
root.iconbitmap('python.ico')
root.geometry("%dx%d+%d+%d"%(600,260,600,250))
# label1=Label(master=root,text="sldfkjsldkfnv", bg="yellow",fg="blue",width=28,height=3,font="tahoma",cursor='heart',anchor="sw",relief=RAISED)
# label1.grid(row=0 ,column=0)
# button1=Button(master=root, text='ok',fg='green',width='20')
# button1.grid(row=1 , column=0, pady=15, columnspan=2)
# button1.bind('<Button>',)

def calcSum(event):
    num1=int(entry1.get())
    num2=int(entry2.get())
    # print(num1+num2)
    messagebox.showinfo("the answer is :" , num1+num2)


entry1=Entry(master=root)
entry1.grid(row=0,column=0, columnspan=3)

entry2=Entry(master=root)
entry2.grid(row=1,column=0, columnspan=3, pady=20)
button1=Button(master=root , text='pluse', width=20)
button1.grid(row=2 , column=0)
button1.bind('<Button>', calcSum)


root.mainloop()