from tkinter import *
root=Tk()
root.title("Ghobad Soltani")
root.iconbitmap('python.ico')
root.geometry("%dx%d+%d+%d"%(600,260,600,250))
label1=Label(master=root,text="sldfkjsldkfnv", bg="yellow",fg="blue",width=28,height=3,font="tahoma",cursor='heart',anchor="sw",relief=RAISED)
message1=Message(root,relief=RAISED,font=('tahoma',20),text='lsdfjlsm,clifnhsdmc alksdjlsndfjnsadfsdlkjvbsakjdnfsdkjfbndj ')
message1.pack()
def fun1():
    label1.config(text='ghobad soltani')




label1.config(text='darsman.com',fg='red',bg='#b1b1b1')
label1.after(5000,fun1)
label1.pack()
frame1=Frame(master=root, bg='blue',width=200,height=300)
frame1.pack()
label2=Label(master=frame1,text='aboli',fg='white',width=150,height=100)
ws=root.wininfo_screenwidth()
hs=root.winfo_screenwidth()
x=(ws/2)-(w/2)
y=(hs/2)-(h/2)
label2.place(width=(x),height=(y))
root.geometry('%dx%d+%d+%d'%(w,h,x,y))
def fun2(event):
    button1.config(text="ghobad")

button1=Button(master=root, text='ok',fg='green',width='20')
button1.bind('<Button>',fun2)
button1.pack()

root.mainloop()