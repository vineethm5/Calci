import tkinter
from tkinter import *

# tkinter._test()
root=tkinter.Tk()
root.geometry("230x230")
root.resizable(0,0)
root.title("My Calculator")
expression=""
input_text = tkinter.StringVar()
# input_text=""
# global expression
def btn_click(item):
    # print(str(item))
    global expression
    expression=expression+str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression=""
    input_text.set("")
    
def btn_calc(item):
    global expression
    try:
        result=str(eval(expression))
        input_text.set("")
        expression=""
        input_text.set(result)
    except:
        input_text.set("enter the wrong arguments")
# input_frame= Frame(root,width=230, height=50)
input_frame= Frame(root,width=230, height=50,highlightthickness=2,highlightbackground="black")
input_frame.pack(side="top")

input_feild=Entry(input_frame,font="arial",justify=RIGHT,textvariable=input_text,width=230)
# input_feild.grid(row=0,column=0)
input_feild.pack(ipady=0)

btn_frame=Frame(root,height=50,width=225,highlightbackground="white")
btn_frame.pack()

clear=Button(btn_frame,text="CLR", width=5,bg="black",fg="white",command=lambda: btn_clear()).grid(row=0,column=0,padx=1,pady=1)
divide=Button(btn_frame,text="/",bg="black",foreground="white", width=5, command=lambda: btn_click("/")).grid(row=0,column=2,padx=1,pady=1)
eqaulto=Button(btn_frame,text="=", width=5, background="black", foreground="white",command=lambda: btn_calc("=")).grid(row=0,column=3,padx=1,pady=1)

# btn_seven=Button(btn_frame,text="7",width=5,background="black",foreground="white", command=lambda:btn_click("7")).grid(row=1,column=0,padx=1,pady=1)
btn_seven = Button(btn_frame, text="7", width=5, background="black", foreground="white", command=lambda: btn_click("7"))
btn_seven.grid(row=1, column=0, padx=1, pady=1)
btn_eight=Button(btn_frame,text="8",width=5,background="black",foreground="white",command=lambda: btn_click("8")).grid(row=1,column=1,padx=1,pady=1)
btn_nine=Button(btn_frame,text="9",width=5,background="black",foreground="white", command=lambda: btn_click("9")).grid(row=1,column=2,padx=1,pady=1)
btn_mul=Button(btn_frame,text="*",width=5,background="black",foreground="white",command=lambda: btn_click("*")).grid(row=1,column=3,padx=1,pady=1)
btn_four=Button(btn_frame,text="4",width=5, background="black", foreground="white",command=lambda: btn_click("4")).grid(row=2,column=0, padx=1,pady=1)
btn_five=Button(btn_frame,text="5",width=5, background="black", foreground="white",command=lambda: btn_click("5")).grid(row=2,column=1, padx=1,pady=1)
btn_six=Button(btn_frame,text="6",width=5, background="black", foreground="white",command=lambda: btn_click("6")).grid(row=2,column=2, padx=1,pady=1)
btn_add=Button(btn_frame,text="+",width=5, background="black", foreground="white",command=lambda: btn_click("+")).grid(row=2,column=3, padx=1,pady=1)
btn_one=Button(btn_frame,text="1",width=5, background="black", foreground="white",command=lambda: btn_click("1")).grid(row=3,column=0, padx=1,pady=1)
btn_two=Button(btn_frame,text="2",width=5, background="black", foreground="white",command=lambda: btn_click("2")).grid(row=3,column=1, padx=1,pady=1)
btn_three=Button(btn_frame,text="3",width=5, background="black", foreground="white",command=lambda:btn_click("3")).grid(row=3,column=2, padx=1,pady=1)
btn_minus=Button(btn_frame,text="-",width=5, background="black", foreground="white",command=lambda: btn_click("-")).grid(row=3,column=3, padx=1,pady=1)
root.mainloop(),