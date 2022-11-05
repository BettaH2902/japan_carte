#############

#prog test deplacement d'image
#03/11/2022
#derniere modif : 03/11/2022
#crea : bettaH

#############







import tkinter as Tk


root = Tk.Tk()

w = 800
h = 650

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

root.geometry('%dx%d+%d+%d' % (w, h, x, y))

cnv = Tk.Canvas(root, width= 400, height= 400, bg = 'black')
cnv.pack()

logo = Tk.PhotoImage(file="Carte/Carte_française/animaux/ane.png")

def show():
    center = (200,200)
    cnv.create_image(center, image=logo)


btn = Tk.Button(cnv, text="suivant", command=show)
btn.pack()


root.mainloop()