from tkinter import *

root=Tk()
root.title("Simple GUI Calculator")
root.geometry("345x460+600+150")
root.resizable(False,False)
root.configure(bg="#17161b")

equation=""

def show(value):
    global equation
    equation+=value
    result_label.config(text=equation)
    

def clear():
    global equation
    equation=""
    result_label.config(text=equation)
    history_label.config(text=equation)


def calculate():
    global equation
    result=""
    if equation!="":
        try:
            result= eval(equation)
        except:
            result="error"
            equation=""

    result_label.config(text=result)
    history_label.config(text=equation)

history_label=Label(root,width=25,height=1,text="",fg="gray",font=("times new roman",20),anchor="e")
history_label.pack()

result_label=Label(root,width=25,height=2,text="",font=("times new roman",30),anchor="e")
result_label.pack()

Button(root,text="C",width=4,height=1,font=("times new roman",20,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda: clear()).place(x=10,y=155)
Button(root,text="/",width=4,height=1,font=("times new roman",20,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("/")).place(x=95,y=155)
Button(root,text="%",width=4,height=1,font=("times new roman",20,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("%")).place(x=180,y=155)
Button(root,text="*",width=4,height=1,font=("times new roman",20,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("*")).place(x=265,y=155)

Button(root,text="7",width=4,height=1,font=("times new roman",20,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("7")).place(x=10,y=215)
Button(root,text="8",width=4,height=1,font=("times new roman",20,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("8")).place(x=95,y=215)
Button(root,text="9",width=4,height=1,font=("times new roman",20,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("9")).place(x=180,y=215)
Button(root,text="-",width=4,height=1,font=("times new roman",20,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("-")).place(x=265,y=215)

Button(root,text="4",width=4,height=1,font=("times new roman",20,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("4")).place(x=10,y=275)
Button(root,text="5",width=4,height=1,font=("times new roman",20,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("5")).place(x=95,y=275)
Button(root,text="6",width=4,height=1,font=("times new roman",20,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("6")).place(x=180,y=275)
Button(root,text="+",width=4,height=1,font=("times new roman",20,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("+")).place(x=265,y=275)

Button(root,text="1",width=4,height=1,font=("times new roman",20,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("1")).place(x=10,y=335)
Button(root,text="2",width=4,height=1,font=("times new roman",20,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("2")).place(x=95,y=335)
Button(root,text="3",width=4,height=1,font=("times new roman",20,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("3")).place(x=180,y=335)

Button(root,text="0",width=9,height=1,font=("times new roman",20,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("0")).place(x=10,y=397)
Button(root,text=".",width=4,height=1,font=("times new roman",20,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show(".")).place(x=180,y=397)
Button(root,text="=",width=4,height=3,font=("times new roman",20,"bold"),bd=1,fg="#fff",bg="#fe9037",command=lambda: calculate()).place(x=265,y=335)



root.mainloop()