from tkinter import *
import time


#draw circle with center in position x and y and radius r
def draw_cir(x,y,r,color):
    cir=can.create_oval(x-r,y-r,x+r,y+r,fill=color)
    return cir
def update_labels(x1,x2,m1,m2,v1,v2,space):
    label_x1 = Label(root, text="x1=         ").place(x=20, y=100)
    label_x1 = Label(root, text="x1= " + str("%.2f" %x1)).place(x=20, y=100)
    label_x2 = Label(root, text="x2=         ").place(x=20, y=150)
    label_x2 = Label(root, text="x2= " + str("%.2f" %x2)).place(x=20, y=150)
    label_v1 = Label(root, text="v1=         ").place(x=20, y=280)
    label_v1 = Label(root, text="v1= " + str("%.2f" % v1)).place(x=20, y=280)
    label_v2 = Label(root, text="v2=         ").place(x=720, y=280)
    label_v2 = Label(root, text="v2= " + str("%.2f" % v2)).place(x=720, y=280)
    label_m1 = Label(root, text="m1=         ").place(x=20, y=380)
    label_m1 = Label(root, text="m1= " + str("%.2f" % m1)).place(x=20, y=380)
    label_m2 = Label(root, text="m2=         ").place(x=720, y=380)
    label_m2 = Label(root, text="m2= " + str("%.2f" % m2)).place(x=720, y=380)
#function which play the simulation
def run():
    global i,index,cir,cir2,x1,x2,rad1,rad2,m1,m2,v1,v2,t,space,y
    global elastic,plastic
    can.delete(cir)
    can.delete(cir2)
    cir = draw_cir(x1, y, rad1, 'red')
    cir2 = draw_cir(x2, y, rad2, 'red')
    if i:
        can.delete(cir)
        can.delete(cir2)
        x1=x1+v1*t
        x2=x2+v2*t
        if elastic==1:
            if abs(x2-x1)<=(rad1+rad2):
                 u2=(2*m1*v1+m2*v2-m1*v2)/(m1+m2)
                 v1=v2+u2-v1
                 v2=u2
        if plastic==1:
            if abs(x2-x1)<=(rad1+rad2):
                 u=(m1*v1+m2*v2)/(m1+m2)
                 v1=u
                 v2=u
        cir = draw_cir(x1,y, rad1, 'red')
        cir2 = draw_cir(x2, y, rad2, 'red')
        #update labels
        update_labels(x1, x2, m1, m2, v1, v2, space)
        root.update()
        time.sleep(0.02)
        can.delete(cir)
        run()
#command when start button clicked
def start_clicked():
    global i
    if i==False:
        i = True
        start_button['text']="stop"
        run()
    elif i==True:
        i = False
        start_button['text'] = "continue"
    update_labels(x1, x2, m1, m2, v1, v2, space)
    set_clicked()

#command when reset button clicked
def reset_clicked():
    global index,space,y
    global i,x1,x2,v1,v2
    global cir,cir2
    i= False
    x1 = x01
    x2 = x02
    v1=v01
    v2=v02
    update_labels(x1, x2, m1, m2, v1, v2, space)
    start_button['text'] = "start"
    can.delete(cir)
    can.delete(cir2)
    cir = draw_cir(x1, y, rad1, 'red')
    cir2 = draw_cir(x2,y, rad2, 'red')

def elastic_clicked():
    global elastic,plastic
    elastic=1
    plastic=0
    plastic_button["bg"] = 'red'
    elastic_button["bg"] = 'green'
def plastic_clicked():
    global elastic,plastic
    elastic=0
    plastic=1
    plastic_button["bg"]='green'
    elastic_button["bg"] = 'red'
def set_clicked():
    global v1,v2,m1,m2,rad1,rad2
    v1=var1.get()
    v2=var2.get()
    m1=var3.get()
    m2=var4.get()
    rad1=20*m1
    rad2=20*m2
    label_v1 = Label(root, text="v1=         ").place(x=20, y=280)
    label_v1 = Label(root, text="v1= " + str("%.2f" % v1)).place(x=20, y=280)
    label_v2 = Label(root, text="v2=         ").place(x=720, y=280)
    label_v2 = Label(root, text="v2= " + str("%.2f" % v2)).place(x=720, y=280)
    label_m1 = Label(root, text="m1=         ").place(x=20, y=380)
    label_m1 = Label(root, text="m1= " + str("%.2f" % m1)).place(x=20, y=380)
    label_m2 = Label(root, text="m2=         ").place(x=720, y=380)
    label_m2 = Label(root, text="m2= " + str("%.2f" % m2)).place(x=720, y=380)
def set_scales():
    global var1,var2,var3,var4
    var1 = DoubleVar()
    var2 = DoubleVar()
    var3 = DoubleVar()
    var4 = DoubleVar()
    scale1 = Scale(root, from_=-300, to=300, orient='horizontal', bg='blue', variable=var1).place(x=0, y=300)
    scale2 = Scale(root, from_=-300, to=300, orient='horizontal', bg='blue', variable=var2).place(x=700, y=300)
    scale3 = Scale(root, from_=1, to=18, orient='horizontal', bg='blue', variable=var3).place(x=0, y=400)
    scale4 = Scale(root, from_=1, to=18, orient='horizontal', bg='blue', variable=var4).place(x=700, y=400)
    set_button = Button(root, text="set", padx=50, bg='white', command=set_clicked).place(x=100, y=500)



i= False    #global variable that tells if the simulation is running or not.
index=0      # global variabels stand for time
x01=100.
x02=500.
x1=x01
x2=x02
y=300  #set the place of the balls on the screen
m1=1
m2=1
rad1=20*m1
rad2=20*m2
v01=0
v02=0
v1=v01
v2=v02
r=50

t=0.05
space=30 #vertical space between labels
elastic=1
plastic=0
root = Tk()
space=20   #vertical space between labels
root.geometry("800x800")
title=Label(root,text= "One dimensional collision",fg='green')
title.config(font=("Courier", 30))
title.pack()
can=Canvas(root,width=600,height=600,background='black')
can.pack()
cir = draw_cir(x1, y, rad1, 'red')
cir2= draw_cir(x2, y, rad2, 'red')
start_button=Button(root,text="start",padx=50,command=start_clicked)
start_button.place(x=200,y=80)
reset_button=Button(root,text="reset",padx=50,command=reset_clicked)
reset_button.place(x=500,y=80)
elastic_button=Button(root,text="elastic",padx=50,bg='green' ,command=elastic_clicked)
elastic_button.place(x=200,y=600)
plastic_button=Button(root,text="plastic",padx=50,bg='red',command=plastic_clicked)
plastic_button.place(x=500,y=600)
#set labels
update_labels(x1, x2, m1, m2, v1, v2, space)
set_scales()

root.mainloop()