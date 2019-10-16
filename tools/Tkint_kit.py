from tkinter import *

fenetre = Tk()

base_cadre = Frame(fenetre, width=500, height=500,borderwidth=2)
cadre2 = Frame(fenetre, width=500, height=500,borderwidth=2)
field_label = Label(base_cadre, text="Coucou")
field_label2 = Label(base_cadre, text="ca roule ?")
bouton_quitter = Button(cadre2, text="Quitter", command=fenetre.quit)

variable_textuelle = StringVar()
ligne_texte = Entry(base_cadre, textvariable=variable_textuelle, width=30)

on_off = IntVar()
checky_breeky = Checkbutton(base_cadre, text="cochez si vous voulez", variable=on_off)
# on peut interroger la variable du checker a traver on_off.get()
# Notez qu'à l'instar d'un bouton, vous pouvez lier la case à cocher à une commande qui sera appelée quand son état change.

un_ou_autre = StringVar()

choix_1 = Radiobutton(base_cadre, text ="1",variable =un_ou_autre, value="option 1")
choix_2 = Radiobutton(base_cadre, text ="2",variable =un_ou_autre, value="option 2")
choix_3 = Radiobutton(base_cadre, text ="3",variable =un_ou_autre, value="option 3")
choix_4 = Radiobutton(base_cadre, text ="4",variable =un_ou_autre, value="option 4")

# Pour récupérer la valeur associée au bouton actuellement sélectionné, interrogez la variable :
# un_ou_autre.get()
liste1 = Listbox(cadre2)

# Pour accéder à la sélection, utilisez la méthodecurselectionde la liste. Elle renvoie un tuple de chaînes de caractères, chacune étant la position de l'élément sélectionné.

# Par exemple, siliste.curselection()renvoie('2',), c'est le troisième élément de la liste qui est sélectionné (Ciseauen l'occurrence).

liste1.insert(END, "Pierre")
liste1.insert(END, "Papier")
liste1.insert(END, "ciseaux")




base_cadre.pack(fill=BOTH)
cadre2.pack(fill=BOTH)
field_label.pack()
field_label2.pack()
ligne_texte.pack()
checky_breeky.pack()
choix_1.pack()
choix_2.pack()
choix_3.pack()
choix_4.pack()
liste1.pack()

bouton_quitter.pack()
fenetre.mainloop()

# A text bloc exist to add text instead of a line

