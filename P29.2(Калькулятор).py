from tkinter import *
btns=[]
root = Tk()
root["bg"] = "black"
root.geometry("485x550+200+200")
root.title("Калькулятор")
root.resizable(False, False)
lbl = Label(text='0', font=("Consolas", 21, "bold"), bg="black", foreground="white")
lbl.place(x=11, y=50)
root.mainloop()