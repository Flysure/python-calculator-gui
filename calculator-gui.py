from tkinter import *
### GUI DEFINITIONS ###
win = Tk()
win.title("Calculator")

def close():
    win.destroy()

def NumPressed(number):
    if number=="C":
        text_space.config(text ="")
    else:
        text_space.config(text = text_space.cget("text")+str(number))


def back():
    text_space.config(text=text_space.cget("text")[:len(text_space.cget("text"))-1])

def Equals():
    functions=["+","-","/","x"]
    for i, c in enumerate(text_space.cget("text")):
        if c in functions:
            firstnum=text_space.cget("text")[0:i]
            secondnum=text_space.cget("text")[i+1:len(text_space.cget("text"))]
            if("." in firstnum or "." in secondnum):
                firstnum=float(firstnum)
                secondnum=float(secondnum)
            else:
                firstnum=int(firstnum)
                secondnum=int(secondnum)

            function=c
            if(c=="+"):
                result=firstnum+secondnum
            elif(c=="-"):
                result=firstnum-secondnum
            elif(c=="x"):
                result=firstnum*secondnum
            elif(c=="/"):
                result=firstnum/secondnum

            if(type(result)==float):
                result = "%.3f" % result

            text_space.config(text =str(result))

buttonC=Button(win,text="C",command=lambda: NumPressed("C"),background="red",height=1,width=1)
buttonC.grid(row=0,column=1)

buttonP=Button(win,text="%",background="red",height=1,width=1)
buttonP.grid(row=0,column=3)
button1 = Button(win,text='7' ,command=lambda: NumPressed("7"),background="red",height=1,width=1)
button1.grid(row=1,column=1)
button2 = Button(win,text='8' ,command=lambda: NumPressed("8"),background="red",height=1,width=1)
button2.grid(row=1,column=2)
button3 = Button(win,text='9' ,command=lambda: NumPressed("9"),background="red",height=1,width=1)
button3.grid(row=1,column=3)
button4 = Button(win,text='4',command=lambda: NumPressed("4"),background="red",height=1,width=1)
button4.grid(row=2,column=1)
button5 = Button(win,text='5',command=lambda: NumPressed("5"),background="red",height=1,width=1)
button5.grid(row=2,column=2)
button6 = Button(win,text='6',command=lambda: NumPressed("6"),background="red",height=1,width=1)
button6.grid(row=2,column=3)
button7 = Button(win,text='1',command=lambda: NumPressed("1"),background="red",height=1,width=1)
button7.grid(row=3,column=1)
button8 = Button(win,text='2',command=lambda: NumPressed("2"),background="red",height=1,width=1)
button8.grid(row=3,column=2)
button9 = Button(win,text='3',command=lambda: NumPressed("3"),background="red",height=1,width=1)
button9.grid(row=3,column=3)
button0 = Button(win,text='      0      ',command=lambda: NumPressed("0"),background="red")
button0.grid(row=4,column=1,columnspan=2)
##Functions
buttonD = Button(win,text="/",command=lambda: NumPressed("/"),background="red",height=1,width=1)
buttonD.grid(row=0,column=4)
buttonM=Button(win,text="x",command=lambda: NumPressed("x"),background="red",height=1,width=1)
buttonM.grid(row=1,column=4)
buttonA=Button(win,text="-",command=lambda: NumPressed("-"),background="red",height=1,width=1)
buttonA.grid(row=2,column=4)
buttonE = Button(win,text='+' ,command=lambda: NumPressed("+"),background="red",height=1,width=1)
buttonE.grid(row=3,column=4)

buttonPo = Button(win,text='.',command=lambda: NumPressed("."),background="red")
buttonPo.grid(row=4,column=3)

buttonba = Button(win,text='<-',command=back,background="red")
buttonba.grid(row=0,column=2)

buttonEq = Button(win,text='=', command=Equals,background="red")
buttonEq.grid(row=4,column=4)

buttonEq = Button(win,text='NextPage', command= lambda: win.show_frame(PageOne),background="red")
buttonEq.grid(row=4,column=5)

text_space=Label(win,text="",fg="red")
text_space.grid(row=5,column=1,columnspan=4)
win.focus_set()

win.bind(".",lambda x:NumPressed("."))
win.bind("0",lambda x:NumPressed("0"))
win.bind("1",lambda x:NumPressed("1"))
win.bind("2",lambda x:NumPressed("2"))
win.bind("3",lambda x:NumPressed("3"))
win.bind("4",lambda x:NumPressed("4"))
win.bind("5",lambda x:NumPressed("5"))
win.bind("6",lambda x:NumPressed("6"))
win.bind("7",lambda x:NumPressed("7"))
win.bind("8",lambda x:NumPressed("8"))
win.bind("9",lambda x:NumPressed("9"))
win.bind("+",lambda x:NumPressed("+"))
win.bind("/",lambda x:NumPressed("/"))
win.bind("-",lambda x:NumPressed("-"))
win.bind("*",lambda x:NumPressed("x"))
win.bind("<Return>",lambda x:Equals())
win.bind("<BackSpace>",lambda x:back())
win.bind("<Shift-BackSpace>",lambda x:NumPressed("C"))
win.bind("z", lambda x:close())

win.mainloop() # Loops forever
