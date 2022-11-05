#coding:utf-8 

#################
"""
page pour ajouter une carte
03/11/2022
derniere modif : 03/11/2022
crea : bettaH
"""
#################

def update_observe(*args):
    pass



import tkinter
from turtle import Screen

if __name__ == "__main__":
    print("yo")

    fenetre = tkinter.Tk()
    Screen_width = fenetre.winfo_screenwidth()
    Screen_height = fenetre.winfo_screenheight()
    print(Screen_width, Screen_height)

    larg = Screen_width / 2
    haut = Screen_height / 2
    pos_x = (Screen_width-larg) / 2
    pos_y = (Screen_height-haut) / 2

    print(larg, haut)

    fenetre.geometry("%dx%d+%d+%d" % (larg,haut,pos_x,pos_y))

   

############ parti a faire en fonction

    #def new_card():
    var_type = tkinter.StringVar()
    var_nom_image_fr = tkinter.StringVar()
    var_nom_image_lang_2 = tkinter.StringVar()

    var_type.trace("w", update_observe)
    var_nom_image_fr.trace("w", update_observe)
    var_nom_image_lang_2.trace("w", update_observe)
        
    label_type = tkinter.Label(fenetre, text="type", font=("Arial",16,"bold")).pack()
    label_type = tkinter.Label(fenetre, text="ろば", font=("Arial",16,"bold")).pack()
    type = tkinter.Entry(fenetre, width = 30, textvariable = var_type,  font=("Arial",12)).pack()
    label_nom_image_fr = tkinter.Label(fenetre, text="nom image fr", font=("Arial",16,"bold")).pack()
    nom_image_fr = tkinter.Entry(fenetre, width = 30, textvariable = var_type,  font=("Arial",12)).pack()
    label_nom_image_lang_2 = tkinter.Label(fenetre, text="nom image dans la seconde lang", font=("Arial",16,"bold")).pack()
    nom_image_2 = tkinter.Entry(fenetre, width = 30, textvariable = var_type,  font=("Arial",12)).pack()

    tkinter.Button(fenetre, text="yo").pack() 


############

    fenetre.mainloop()