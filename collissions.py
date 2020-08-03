from tkinter import *
import time


#draw circle with center in position x and y and radius r
def draw_cir(x,y,r,color):
    cir=can.create_oval(x-r,y-r,x+r,y+r,fill=color)
    return cir
def update_labels(x1,x2,m1,m2,v1,v2,space):
    label_x1 = Label(root, text="x1=         ").place(x=20, y=space+100)
    label_x1 = Label(root, text="x1= " + str("%.2f" %x1)).place(x=20, y=space+100)
    label_x2 = Label(root, text="x2=         ").place(x=20, y=space*2+100)
    label_x2 = Label(root, text="x2= " + str("%.2f" %x2)).place(x=20, y=space*2+100)
    label_m1 = Label(root, text="m1=         ").place(x=20, y=space*3+100)
    label_m1 = Label(root, text="m1= " + str("%.2f" %m1)).place(x=20, y=space*3+100)
    label_m2 = Label(root, text="m2=         ").place(x=20, y=space*4+100)
    label_m2 = Label(root, text="m2= " + str("%.2f" %m2)).place(x=20, y=space*4+100)
    label_v1 = Label(root, text="v1=         ").place(x=20, y=space * 5 + 100)
    label_v1 = Label(root, text="v1= " + str("%.2f" %v1)).place(x=20, y=space * 5 + 100)
    label_v2 = Label(root, text="v2=         ").place(x=20, y=space * 6 + 100)
    label_v2 = Label(root, text="v2= " + str("%.2f" %v2)).place(x=20, y=space * 6 + 100)
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
i= False    #global variable that tells if the simulation is running or not.
index=0      # global variabels stand for time
x01=100.
x02=500.
x1=x01
x2=x02
y=300  #set the place of the balls on the screen
rad1=20
rad2=20
v01=25.
v02=-30.
v1=v01
v2=v02
r=50
m1=1
m2=0.5
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

'''w = Scale(from_=-100, to=100,orient='horizontal',bg='blue')
w.place(x=100,y=400)'''

root.mainloop()