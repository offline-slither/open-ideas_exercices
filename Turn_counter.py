
from tkinter import *

fenetre = Tk()
# count_val = IntVar()
# countstring = StringVar()
disp_nbturn = StringVar()
nbturn = 0
count_val = 0
disp_nbturn.set("0")

def incr_count():
	global nbturn
	nbturn += 1
	disp_nbturn.set(f" {nbturn} ")

def dcr_count():
	global nbturn
	nbturn -= 1
	if nbturn < 0: nbturn = 0
	disp_nbturn.set(f" {nbturn} ")

def c_reset():
	global nbturn
	nbturn = 0
	disp_nbturn.set(f" {nbturn} ")

# disp_nbturn.set(f" {nbturn} ")


# field_label = Label(fenetre, text="pile ou face")
field_label = Label(fenetre, text="Tours")
mainbutton = Button(fenetre,text=" + ", command=incr_count)
sidebutton = Button(fenetre,text=" - ", command=dcr_count)
t_count = Label(fenetre, textvariable=disp_nbturn)
Reset = Button(fenetre,text=" Reset ", command=c_reset)


field_label.pack()
mainbutton.pack()
sidebutton.pack()
t_count.pack()
Reset.pack()
fenetre.mainloop()