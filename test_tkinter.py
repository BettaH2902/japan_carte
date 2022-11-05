
import tkinter as Tk


wind = Tk.Tk()
bt_yes = Tk.Button(wind, text="test")

height_screen = wind.winfo_screenheight()
width_screen = wind.winfo_screenwidth()

print(width_screen, height_screen)

bt_yes.pack()


wind.geometry()
wind.mainloop()