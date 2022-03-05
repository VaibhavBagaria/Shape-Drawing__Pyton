from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msgbox
root=Tk()
root.title("Shape Drawing App")
root.geometry("800x800")
root.configure(bg='lightblue')


text_L1=Label(root,text="Color:",bg="lightblue")
text_L1.place(relx=0.6,rely=0.8,anchor=CENTER) 
input_color=Entry(root,width=10)
input_color.insert(0,"blue")
input_color.place(relx=0.7,rely=0.8,anchor=CENTER)

text_L3=Label(root,text="StartX:",bg="lightblue")
text_L3.place(relx=0.05,rely=0.73,anchor=CENTER) 
input_Sx=Entry(root,width=10)
input_Sx.insert(0,"200")
input_Sx.place(relx=0.15,rely=0.73,anchor=CENTER)


text_L3=Label(root,text="StartY:",bg="lightblue")
text_L3.place(relx=0.25,rely=0.73,anchor=CENTER) 
input_Sy=Entry(root,width=10)
input_Sy.insert(0,"200")
input_Sy.place(relx=0.35,rely=0.73,anchor=CENTER)


text_L4=Label(root,text="EndX:",bg="lightblue")
text_L4.place(relx=0.45,rely=0.73,anchor=CENTER) 
input_Ex=Entry(root,width=10)
input_Ex.insert(0,"400")
input_Ex.place(relx=0.55,rely=0.73,anchor=CENTER)


text_L5=Label(root,text="EndY:",bg="lightblue")
text_L5.place(relx=0.65,rely=0.73,anchor=CENTER) 
input_Ey=Entry(root,width=10)
input_Ey.insert(0,"400")
input_Ey.place(relx=0.75,rely=0.73,anchor=CENTER)


canvas=Canvas(root,width=400,height=400, bg="white",highlightthickness=5,borderwidth=2,relief=SOLID)
canvas.pack()
    
shape_name=""
def draw_circle(event):
    global shape_name
    oldx=input_Sx.get()
    oldy=input_Sy.get()
    newy=input_Ex.get()
    newx=input_Ey.get()
    shape_name="Circle"
    keypress="c"
    drawshape(keypress,oldx,oldy,newx,newy)

def draw_square(event):
    global shape_name
    oldx=input_Sx.get()
    oldy=input_Sy.get()
    newy=input_Ex.get()
    newx=input_Ey.get()
    shape_name="Square"
    keypress="s"
    drawshape(keypress,oldx,oldy,newx,newy)

def draw_rect(event):
    global shape_name
    oldx=input_Sx.get()
    oldy=input_Sy.get()
    newy=input_Ex.get()
    newx=input_Ey.get()
    shape_name="Rectangle"
    keypress="r"
    drawshape(keypress,oldx,oldy,newx,newy)


def drawshape(keypress,oldx,oldy,newx,newy) :
    global shape_name
    color_name=input_color.get()
    if(keypress=="s"):
        shape_name=canvas.create_rectangle(oldx, oldy, newx, newy, fill=str(color_name), outline = str(color_name))
        
    if(keypress=="r"):
        shape_name=canvas.create_rectangle(oldx, oldy, newx, newy, fill=str(color_name), outline = str(color_name))
        
    if(keypress=="c"):
        print("circle")
        shape_name=canvas.create_oval(oldx, oldy, newx, newy, fill=str(color_name))
        
root.bind("<c>",draw_circle)
root.bind("<s>",draw_square)
root.bind("<r>",draw_rect)

root.mainloop() 

